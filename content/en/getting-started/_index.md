---
title: "Getting Started"
icon: "🚀"
weight: -20
---

## Background

Prescriptive process monitoring is a monitoring method that predicts potential failure cases by tracking and analyzing business processes, and provides corresponding recommendations to achieve expected results. The term "prescriptive" means that this method provides prescription-like advice to process operators, and if they adopt these suggestions, the probability of case success will be higher. The success or failure of a case is calculated based on some metrics like key performance indicators (KPIs) defined by enterprise and domain experts. Therefore, the goal of prescriptive process monitoring is to help enterprises make wiser decisions during process execution in order to improve efficiency and productivity.

## Introduction

PrCore is a backend software that offers APIs to implement certain features of prescriptive process monitoring. It allows users to upload event logs and provides definitions, which can then be used to train models based on historical data. When users submit new logs, PrCore is capable of providing different types of prescriptions for ongoing cases.

Users can obtain results for all cases in the logs by uploading new log files. In addition, sending stream data of new events through APIs allows users to receive timely prescribing recommendations from PrCore.

PrCore uses a modular design that makes adding new machine learning algorithms to the program an easy task. This allows researchers to effortlessly add new plugins according to the documentation, providing other categories of prescriptions for testing algorithms of interest.

Overall, PrCore is a tool that enables prescriptive process monitoring and offers users an efficient and customizable way to analyze event logs and improve their processes.

## Use Case

{{< link "Kairos" "https://github.com/VisualPM" >}} is a prescriptive process monitoring interface that uses PrCore as a backend to get prescriptions. It provides a user-friendly interface for users to upload event logs and receive prescriptions.

## User Guide

Please follow guides below to get started with PrCore:

{{< toc-tree >}}
