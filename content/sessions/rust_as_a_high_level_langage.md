---
key: rust_as_a_high_level_langage
title: Rust as a High-Level Langage
id: PjQDGsFIQoo1By4Ogv3q
language: English
format: conference
tags:
  - _languages
level: beginner
speakers:
  - aleksey_kladov
videoId: AAr6uALbYY0
presentation: null
draft: false
---
The singe most important feature of Rust is memory safety. Writing code with performance of C++, at a typical development cost, and with guaranteed absence of certain classes of memory safety related vulnerabilities is something that was not possible before. 

However, all popular managed languages with garbage collection take memory safety for granted, so this aspect of Rust doesn't bring anything new to the table, if you already use Java or Go. Nevertheless, Rust can be an interesting choice as a high-level language, and this talks explains way.  

The focus of the talk is fearless concurrency. Data races are a pervasive and unsolved problem in languages like Java and Rust's guaranteed thread safety is a liberating experience for application development. We also touch on some other benefits of the language for high-level tasks:

* predictable performance due to absence of garbage  collection
*  control over the memory layout of objects, which gives you extra performance if you need it
*  module (crate) system that, at the language level, prevents dependency hell
* additional correctness guarantees, like the absence of iterator validation or strict control of error conditions
