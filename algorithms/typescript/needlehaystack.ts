import { assert } from './assert'

function strStr(haystack: string, needle: string) {
  for (let i = 0; i < haystack.length; i++) {
    if (needle === haystack.substr(i, needle.length)) {
      return i
    }
  }
  return -1
}

assert(
  strStr('hello world', 'llo') === 2,
  strStr('hello world', 'llo').toString()
)
