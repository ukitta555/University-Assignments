//
// Created by vlad on 25.05.22.
//
//
// Created by vlad on 24.05.22.
//

#include <iostream>
#include <chrono>
#include <thread>
#include <mutex>
#include <semaphore>
#include <random>

const int N = 5;          // number of philosophers
enum {
  THINKING=0,             // philosopher is thinking
  HUNGRY=1,               // philosopher is trying to get forks
  EATING=2,               // philosopher is eating
};

#define LEFT (i+N-1)%N    // number of i's left neighbor
#define RIGHT (i+1)%N     // number of i's right neighbor

int state[N];             // array to keep track of everyone's state
std::mutex mutex_;        // mutual exclusion for critical regions
std::binary_semaphore s[N]{
    std::binary_semaphore(0),
    std::binary_semaphore(0),
    std::binary_semaphore(0),
    std::binary_semaphore(0),
    std::binary_semaphore(0),
};
                          // one semaphore per philosopher
std::mutex mo;            // for synchronized cout

int myrand(int min, int max) {
  static std::mt19937 rnd(std::time(nullptr));
  return std::uniform_int_distribution<>(min,max)(rnd);
}

void test(int i) {        // i: philosopher number, from 0 to N-1
  if (state[i] == HUNGRY
   && state[LEFT] != EATING && state[RIGHT] != EATING) {
    state[i] = EATING;
    s[i].release();
  }
}

void think(int i) {
  int duration = myrand(400, 800);
  {
    std::lock_guard<std::mutex> gmo(mo);
    std::cout<<i<<" thinks "<<duration<<"ms\n";
  }
  std::this_thread::sleep_for(std::chrono::milliseconds(duration));
}

void take_forks(int i) {  // i: philosopher number, from 0 to N-1
  mutex_.lock();          // enter critical region
  state[i] = HUNGRY;      // record fact that philosopher i is hungry
  {
    std::lock_guard<std::mutex> gmo(mo);
    std::cout<<"\t\t"<<i<<" is hungry\n";
  }
  test(i);                // try to acquire 2 forks
  mutex_.unlock();        // exit critical region
  s[i].acquire();         // block if forks were not acquired
}

void eat(int i) {
  int duration = myrand(400, 800);
  {
    std::lock_guard<std::mutex> gmo(mo);
    std::cout<<"\t\t\t\t"<<i<<" eats "<<duration<<"ms\n";
  }
  std::this_thread::sleep_for(std::chrono::milliseconds(duration));
}

void put_forks(int i) {   // i: philosopher number, from 0 to N-1
  mutex_.lock();          // enter critical region
  state[i] = THINKING;    // philosopher has finished eating
  test(LEFT);           // see if left neighbor can now eat
  test(RIGHT);          // see if right neighbor can now eat
  mutex_.unlock();        // exit critical region
}

void philosopher(int i) { // i: philosopher number, from 0 to N-1
  while (true) {          // repeat forever
    think(i);             // philosopher is thinking
    take_forks(i);        // acquire two forks or block
    eat(i);               // yum-yum, spaghetti
    put_forks(i);         // put both forks back on table
  }
}

int main() {
  std::cout<<"dp_14\n";

  std::thread t0([&] {philosopher(0);});
  std::thread t1([&] {philosopher(1);});
  std::thread t2([&] {philosopher(2);});
  std::thread t3([&] {philosopher(3);});
  std::thread t4([&] {philosopher(4);});
  t0.join();
  t1.join();
  t2.join();
  t3.join();
  t4.join();
}
