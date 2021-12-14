################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
CPP_SRCS += \
../src/Nata2.cpp \
../src/bus_manager.cpp \
../src/main.cpp \
../src/query.cpp \
../src/responses.cpp 

OBJS += \
./src/Nata2.o \
./src/bus_manager.o \
./src/main.o \
./src/query.o \
./src/responses.o 

CPP_DEPS += \
./src/Nata2.d \
./src/bus_manager.d \
./src/main.d \
./src/query.d \
./src/responses.d 


# Each subdirectory must supply rules for building sources it contributes
src/%.o: ../src/%.cpp
	@echo 'Building file: $<'
	@echo 'Invoking: Cross G++ Compiler'
	g++ -O0 -g3 -Wall -c -fmessage-length=0 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


