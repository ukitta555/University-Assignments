//
// Created by vlad on 29.05.22.
//
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <iostream>
#include <signal.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/msg.h>

bool f(int);
bool g(int);

// structure for message queue
struct mesg_buffer {
    long mesg_type;
    int value;
};

int get_first_queue(){
    int key_one = ftok("progfile", 65);
    return msgget(key_one, 0666 | IPC_CREAT);
}

int get_second_queue() {
    int key_two = ftok("progfile", 66);
    return msgget(key_two, 0666 | IPC_CREAT);
}

int main(int argc, char** argv)
{
    int res1 = -1;
    int res2 = -1;

    int status1 = 0;
    int status2 = 0;

    int x;
    printf("Enter data:\n");
    scanf("%d", &x);

    pid_t firstChild, secondChild;

    mesg_buffer msg1, msg2, resp1, resp2;
    msg1.mesg_type = 1;
    msg2.mesg_type = 1;

    int first_queue = get_first_queue();
    int second_queue = get_second_queue();

    int child_queue;

    if((firstChild = fork()) < 0)
    {
        perror("Can't fork process");
        exit(EXIT_FAILURE);
    }

    if(firstChild == 0)
    {
        mesg_buffer message;
        msgrcv(first_queue, &message, sizeof(message), 1, 0);

        printf("Child 1 received %d\n", message.value);
        res1 = f(message.value);


        mesg_buffer response = {2, res1};
        msgsnd(first_queue, &response, sizeof(response), 0);
        printf("Child 1 send %d\n", res1);

        exit(EXIT_SUCCESS);
    }
    else
    {

        msg1.value = x;
        msg2.value = x;
        msgsnd(first_queue, &msg1, sizeof(msg1), 0);
        msgsnd(second_queue, &msg2, sizeof(msg2), 0);

        if((secondChild = fork()) < 0)
        {
            perror("Can't fork process");
            exit(EXIT_FAILURE);
        }

        if(secondChild == 0)
        {
            mesg_buffer message;
            msgrcv(second_queue, &message, sizeof(message), 1, 0);


            printf("Child 2 received %d\n", message.value);
            res2=g(message.value);


            mesg_buffer response = {2, res2};
            msgsnd(second_queue, &response, sizeof(response), 0);
            printf("Child 2 send %d\n", res2);

            exit(EXIT_SUCCESS);
        }
        else
        {
            int time = 1;
            bool firstComplete = false;
            bool secondComplete = false;
            while (true)
            {
                // WNOHANG - негайно вертає управління, якщо жоден дочірній процес не завершився
                pid_t firstCheck = waitpid(firstChild, &status1, WNOHANG);
                pid_t secondCheck = waitpid(secondChild, &status2, WNOHANG);


                std::cout << "Statuses: " << std::endl <<
                "First: " << firstCheck << ' ' <<
                "Second: " << secondCheck << std::endl;

                if(firstCheck > 0) firstComplete = true;
                if(secondCheck > 0) secondComplete = true;

                if(firstComplete && secondComplete)
                {
                    break;
                }

                if (firstComplete && res1 == -1) {
                    printf("Getting f result \n");
                    msgrcv(first_queue, &resp1, sizeof(resp1), 2, 0);
                    res1 = resp1.value;
                    printf("Received f value: %d \n", res1);
                    if (resp1.value == 1) {
                        printf("f(x)=1 and g(x)=undefined\n");
                        printf("Result: 1 || undefined = 1\n");
                        msgctl(first_queue, IPC_RMID, NULL);
                        msgctl(second_queue, IPC_RMID, NULL);
                        printf("Killing second child \n");
                        kill(secondChild, SIGKILL);
                        exit(0);
                    }
                    else {
                    }
                }

                if (secondComplete && res2 == -1) {
                    printf("Getting g result \n");
                    msgrcv(second_queue, &resp2, sizeof(resp2), 2, 0);
                    res2 = resp2.value;
                    printf("Received g value: %d \n", res2);
                    if (resp2.value == 1) {
                        printf("f(x)=undefined and g(x)=1\n");
                        printf("Result: undefined || 1 = 1\n");

                        msgctl(first_queue, IPC_RMID, NULL);
                        msgctl(second_queue, IPC_RMID, NULL);
                        printf("Killing first child: \n");
                        kill(firstChild, SIGKILL);
                        exit(0);
                    }
                }

                if(time % 5 == 0)
                {
                    printf("Do you want to continue calculations: y\\n?\n");
                    char response;
                    scanf(" %c", &response);
                    if(response != 'y')
                    {
                        printf("Killing everything \n");
                        msgctl(first_queue, IPC_RMID, NULL);
                        msgctl(second_queue, IPC_RMID, NULL);
                        kill(firstChild, SIGKILL);
                        kill(secondChild, SIGKILL);
                        exit(0);
                    }
                }
                sleep(1);
                time++;
            }

            if (res1 == -1) {
                msgrcv(first_queue, &resp1, sizeof(resp1), 2, 0);
            }
            if (res2 == -1) {
                msgrcv(second_queue, &resp2, sizeof(resp2), 2, 0);
            }


            msgctl(first_queue, IPC_RMID, NULL);
            msgctl(second_queue, IPC_RMID, NULL);

            printf("f(x)=%d and g(x)=%d\n", resp1.value, resp2.value);
            printf("Result: %d || %d = %d\n", resp1.value, resp2.value, resp1.value || resp2.value);
        }
    }
}


bool f(int x)
{
    if(x < 0) return false;
    if (x == 0) return false;
    if (x > 0) while (true) {
        sleep(1);
    }
}

bool g(int x)
{
    if(x < 0) while (true) {
        sleep(1);
    }
    if (x == 0) return true;
    if (x > 0) return true;
}