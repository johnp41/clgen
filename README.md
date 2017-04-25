# My PhD

A self-contained, monolothic repository for (almost) everything I have done while at the University of Edinburgh. Living an #open life.


##  Publications

1. Chris Cummins, Pavlos Petoumenos, Zheng Wang, Hugh Leather.
   "**Synthesizing Benchmarks for Predictive Modeling**".
   CGO '17.
   [[source code]](https://github.com/ChrisCummins/paper-synthesizing-benchmarks/).
   [[pdf]](https://github.com/ChrisCummins/paper-synthesizing-benchmarks/raw/master/paper.pdf).
   Build command: `$ bazel build //docs:2017-02-cgo`.
1. Chris Cummins, Pavlos Petoumenos, Michel Steuwer, Hugh Leather.
   "**Autotuning OpenCL Workgroup Sizes**". ACACES '16. [[source
   code]](/docs/2016-07-acaces). Build command: `$ bazel build
   //docs:2016-07-acaces`.
1. Chris Cummins, Pavlos Petoumenos, Michel Steuwer, Hugh Leather.
   "**Towards Collaborative Performance Tuning of Algorithmic Skeletons**".
   HLPGPU '16, HiPEAC.
   [[source code]](https://github.com/ChrisCummins/paper-towards-collaborative-performance-tuning).
   [[pdf]](https://github.com/ChrisCummins/paper-towards-collaborative-performance-tuning/raw/master/paper.pdf).
   Build command: `$ bazel build //docs:2016-01-hlpgpu`.
1. Chris Cummins, Pavlos Petoumenos, Michel Steuwer, Hugh Leather.
   "**Autotuning OpenCL Workgroup Size for Stencil Patterns**".
   ADAPT '16, HiPEAC.
   [[source code]](https://github.com/ChrisCummins/paper-autotuning-opencl-wgsize).
   [[pdf]](https://github.com/ChrisCummins/paper-autotuning-opencl-wgsize/raw/master/paper.pdf).
   Build command: `$ bazel build //docs:2016-01-adapt`.
1. Chris Cummins. "**Autotuning Stencils Codes with Algorithmic Skeletons**".
   MSc Thesis, 2015. The University of Edinburgh.
   [[source code]](/docs/2015-08-msc-thesis).
   Build command: `$ bazel build //docs:2015-08-msc-thesis`.


## Talks

1. Chris Cummins. "**Using Deep Learning to Generate Human-like Code**", 22nd
   April, 2017. Scottish Programming Languages Seminar, University of St.
   Andrews, Scotland. [[files]](/talks/2017-03-spls).
1. Chris Cummins. "**Synthesizing Benchmarks for Predictive Modeling**", 6th
   Febuary, 2017. International Symposium on Code Generationand Optimization
   (CGO), Austin, Texas, USA. [[files]](/talks/2017-02-cgo).
   [[slides]](https://speakerdeck.com/chriscummins/synthesizing-benchmarks-for-predictive-modelling-cgo-17).
1. Chris Cummins. "**Machine Learning & Compilers**", 9th September, 2016.
   Codeplay, Edinburgh, Scotland. [[files]](/talks/2017-02-cgo).
   [[slides]](https://speakerdeck.com/chriscummins/machine-learning-and-compilers).
1. Chris Cummins. "**Building an AI that Codes**", 22nd July, 2016.  Ocado
   Technology, Hatfield, England. [[files]](/talks/2016-07-ocado).
1. Chris Cummins.
   "**All the OpenCL on GitHub: Teaching an AI to code, one character at a time**",
   19th May, 2016. Amazon Development Centre, Edinburgh, Scotland.
   [[files]](/talks/2016-05-amazon).
1. Chris Cummins. "**Autotuning and Algorithmic Skeletons**", Wed 10th Feb,
   2016. The University of Edinburgh, Scotland. [[files]](/talks/2016-02-ppar).
1. Chris Cummins. "**Towards Collaborative Performance Tuning of Algorithmic
   Skeletons**", Tues 19th Jan, 2016. HLPGPU, HiPEAC, Prague.
   [[files]](/talks/2016-01-hlpgpu).
1. Chris Cummins. "**Autotuning OpenCL Workgroup Size for Stencil Patterns**",
   Mon 18th Jan, 2016. ADAPT, HiPEAC, Prague. Files:
   [[files]](/talks/2016-01-adapt).
1. Chris Cummins.
   "**Towards Collaborative Performance Tuning of Algorithmic Skeletons**",
   Thurs 14th Jan, 2016. CArD talk, University of Edinburgh.
   [[files]](/talks/2016-01-hlpgpu).


## Misc

1. Chris Cummins, Pavlos Petoumenos, Michel Steuwer, Hugh Leather.
   "**Collaborative Autotuning of Algorithmic Skeletons for GPUs and CPUs**".
   Incomplete journal version of ADAPT and HLPGPU papers.
   [[source code]](/docs/2016-12-wip-taco).
   Build command: `$ bazel build //docs:2016-12-wip-taco`.
1. Chris Cummins. "**Deep Learning for Compilers**". PhD First Year Review
   Document, 2016. [[source code]](/docs/2016-11-first-year-review).
   Build command: `$ bazel build //docs:2016-11-first-year-review`.
1. Chris Cummins, Hugh Leather. "**Autotuning OpenCL Workgroup Sizes**".
   Rejected submission for PACT'16 Student Research Competition.
   [[source code]](/docs/2016-07-pact).
   Build command: `$ bazel build //docs:2016-07-pact`.
1. Chris Cummins, Pavlos Petoumenos, Michel Steuwer, Hugh Leather. "Autotuning
   OpenCL Workgroup Sizes". Submission for PLDI'16 Student Poster Session.
   [[source code]](/docs/2016-06-pldi).
   Build command: `$ bazel build //docs:2016-06-pldi`.
1. Chris Cummins. "Autotuning and Skeleton-aware Compilation". PhD Progression
   Review, 2015. [[source code]](/docs/2015-09-progression-review).
   Build command: `$ bazel build //docs:2015-09-progression-review`.


<h2>
   Building the code
   <a href="https://travis-ci.org/ChrisCummins/phd" target="_blank">
    <img src="https://img.shields.io/travis/ChrisCummins/phd/master.svg?style=flat">
  </a>
</h2>


### Requirements

* Ubuntu 16.04 or macOS.
* OpenCL.


### Installation

The script `./tools/bootstrap.sh` will probe your system for the required packages, and if any are missing, print the commands necessary to install them. Automatically install them using:

```sh
$ ./tools/bootstrap.sh | bash
```

Test the universe using:

```
$ bazel test //...
```
