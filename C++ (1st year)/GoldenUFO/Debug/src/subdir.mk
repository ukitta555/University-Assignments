################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
CPP_SRCS += \
../src/Boolba.cpp \
../src/GoldenBlock.cpp \
../src/GoldenUFO.cpp \
../src/Zolotosyorb.cpp \
../src/fib.cpp \
../src/loopSearch.cpp \
../src/rnd.cpp 

OBJS += \
./src/Boolba.o \
./src/GoldenBlock.o \
./src/GoldenUFO.o \
./src/Zolotosyorb.o \
./src/fib.o \
./src/loopSearch.o \
./src/rnd.o 

CPP_DEPS += \
./src/Boolba.d \
./src/GoldenBlock.d \
./src/GoldenUFO.d \
./src/Zolotosyorb.d \
./src/fib.d \
./src/loopSearch.d \
./src/rnd.d 


# Each subdirectory must supply rules for building sources it contributes
src/%.o: ../src/%.cpp
	@echo 'Building file: $<'
	@echo 'Invoking: Cross G++ Compiler'
	g++ -O0 -g3 -Wall -c -fmessage-length=0 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


