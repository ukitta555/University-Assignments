################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
CPP_SRCS += \
../src/LR10.cpp \
../src/MonteCarlo.cpp \
../src/Triangle.cpp \
../src/circle.cpp \
../src/square.cpp 

OBJS += \
./src/LR10.o \
./src/MonteCarlo.o \
./src/Triangle.o \
./src/circle.o \
./src/square.o 

CPP_DEPS += \
./src/LR10.d \
./src/MonteCarlo.d \
./src/Triangle.d \
./src/circle.d \
./src/square.d 


# Each subdirectory must supply rules for building sources it contributes
src/%.o: ../src/%.cpp
	@echo 'Building file: $<'
	@echo 'Invoking: Cross G++ Compiler'
	g++ -O0 -g3 -Wall -c -fmessage-length=0 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


