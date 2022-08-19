package com.example.adminjsp.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;

@Configuration
public class PersistenceConfig {

    @Bean
    public ManagedChannel getManagedChannel() {
        ManagedChannel channel = ManagedChannelBuilder.forTarget("127.0.0.1:50051")
                .usePlaintext()
                .build();

        return channel;
    }

}
