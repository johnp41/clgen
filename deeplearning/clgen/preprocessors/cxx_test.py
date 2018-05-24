"""Unit tests for ///cxx_test."""
import sys

import pytest
from absl import app
from absl import flags

from deeplearning.clgen import errors
from deeplearning.clgen.preprocessors import cxx


FLAGS = flags.FLAGS


# ClangPreprocess() tests.

def test_ClangPreprocess_empty_input():
  """Test that ClangPreprocess accepts an empty input."""
  assert cxx.ClangPreprocess('') == '\n'


def test_ClangPreprocess_small_cxx_program():
  """Test pre-processing a small C++ program."""
  assert cxx.ClangPreprocess("""
#define FOO T
template<typename FOO>
FOO foobar(const T& a) {return a;}

int foo() { return foobar<int>(10); }
""") == """

template<typename T>
T foobar(const T& a) {return a;}

int foo() { return foobar<int>(10); }
"""


# Compile() tests.

def test_Compile_empty_input():
  """Test that Compile accepts an empty input."""
  assert cxx.Compile('') == ''


def test_Compile_small_cxx_program():
  """Test Compile on a small C++ program."""
  assert cxx.Compile("""
#define FOO T
template<typename FOO>
FOO foobar(const T& a) {return a;}

int foo() { return foobar<int>(10); }
""") == """
#define FOO T
template<typename FOO>
FOO foobar(const T& a) {return a;}

int foo() { return foobar<int>(10); }
"""


def test_Compile_user_define():
  """Test that Compile accepts a program with a custom #define."""
  assert cxx.Compile("""
#define FLOAT_T float
int A(FLOAT_T* a) {}
""") == """
#define FLOAT_T float
int A(FLOAT_T* a) {}
"""


def test_Compile_syntax_error():
  """Test that Compile rejects a program with invalid syntax."""
  with pytest.raises(errors.ClangException) as e_info:
    cxx.Compile("int mainA2@@1!!!#")
  assert 'error: ' in str(e_info.value)


def test_Compile_undefined_variable():
  """Test that Compile rejects a program with an undefined variable."""
  with pytest.raises(errors.ClangException) as e_info:
    cxx.Compile("""
int main(int argc, char** argv) {
  undefined_variable;
}
""")
  assert 'use of undeclared identifier' in str(e_info.value)


def test_Compile_undefined_function():
  """Test that Compile rejects a program with an undefined function."""
  with pytest.raises(errors.ClangException) as e_info:
    cxx.Compile("""
int main(int argc, char** argv) {
  undefined_function(argc);
}
""")
  assert 'use of undeclared identifier' in str(e_info.value)


# StripComments() tests.

def test_StripComments_empty_input():
  """Test StripComments on an empty input."""
  assert cxx.StripComments('') == ''


def test_StripComments_only_comment():
  """Test StripComments on an input containing only comments."""
  assert cxx.StripComments('// Just a comment') == ' '
  assert cxx.StripComments('/* Just a comment */') == ' '


def test_StripComments_small_program():
  """Test Strip Comments on a small program."""
  assert cxx.StripComments("""
/* comment header */

int main(int argc, char** argv) { // main function.
  return /* foo */ 0;
}
""") == """
 

int main(int argc, char** argv) {  
  return   0;
}
"""


# Benchmarks.

HELLO_WORLD_CXX = """
#include <iostream>

int main(int argc, char** argv) {
  std::cout << "Hello, world!" << std::endl;
  return 0;
}
"""


def test_benchmark_ClangPreprocess_hello_world(benchmark):
  """Benchmark ClangPreprocess on a "hello world" C++ program."""
  benchmark(cxx.ClangPreprocess, HELLO_WORLD_CXX)


def test_benchmark_Compile_hello_world(benchmark):
  """Benchmark Compile on a "hello world" C++ program."""
  benchmark(cxx.Compile, HELLO_WORLD_CXX)


def test_benchmark_StripComments_hello_world(benchmark):
  """Benchmark StripComments on a "hello world" C++ program."""
  benchmark(cxx.StripComments, HELLO_WORLD_CXX)


def main(argv):
  """Main entry point."""
  del argv
  sys.exit(pytest.main([__file__, '-v']))


if __name__ == '__main__':
  app.run(main)
