package com.example.adminjsp.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.ResponseBody;

import com.example.adminjsp.rpcservice.Book.BookRequest;
import com.example.adminjsp.rpcservice.Book.BookResponse;
import com.example.adminjsp.rpcservice.Book.SimpleRequest;
import com.example.adminjsp.rpcservice.Book.SimpleResponse;
import com.example.adminjsp.rpcservice.BookServiceGrpc;
import com.example.adminjsp.rpcservice.BookServiceGrpc.BookServiceBlockingStub;
import com.googlecode.protobuf.format.JsonFormat;

import io.grpc.ManagedChannel;

@Controller
public class AdminController {

    private ManagedChannel channelToPythonServer;
    private final BookServiceBlockingStub stub;

    AdminController(ManagedChannel managedChannel) {
        channelToPythonServer = managedChannel;
        stub = BookServiceGrpc.newBlockingStub(channelToPythonServer);
    }

    @GetMapping("/")
    public String adminMain() {
        return "index";
    }

    @GetMapping("/rpc/dash")
    @ResponseBody
    public String rpctest() {
        System.out.println("hey");
        BookResponse res = stub.getBooksByBookName(BookRequest.newBuilder().setMessage("dashboard").build());

        return new JsonFormat().printToString(res);
    }

    @GetMapping("/rpc/pythonChart")
    @ResponseBody
    public String pythonChart() {
        SimpleResponse res = stub.execPythonMLModel(SimpleRequest.newBuilder().setMessage("").build());

        return new JsonFormat().printToString(res);
    }

}
