function assert(expr) {
  if (!expr) {
    throw new Error('AssertionError')
  }
}
