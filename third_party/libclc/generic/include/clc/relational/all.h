#define _CLC_ALL_DECL(TYPE) _CLC_OVERLOAD _CLC_DECL int all(TYPE v);

#define _CLC_VECTOR_ALL_DECL(TYPE) \
  _CLC_ALL_DECL(TYPE)              \
  _CLC_ALL_DECL(TYPE##2)           \
  _CLC_ALL_DECL(TYPE##3)           \
  _CLC_ALL_DECL(TYPE##4)           \
  _CLC_ALL_DECL(TYPE##8)           \
  _CLC_ALL_DECL(TYPE##16)

_CLC_VECTOR_ALL_DECL(char)
_CLC_VECTOR_ALL_DECL(short)
_CLC_VECTOR_ALL_DECL(int)
_CLC_VECTOR_ALL_DECL(long)

#undef _CLC_ALL_DECL
#undef _CLC_VECTOR_ALL_DECL
