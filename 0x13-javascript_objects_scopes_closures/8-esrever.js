#!/usr/bin/node

exports.esrever = function (list) {
  let len = list.length - 1;
  let i = 0;
  while ((len - i) > 0) {
    const swap = list[len];
    list[len] = list[i];
    list[i] = swap;
    i++;
    len--;
  }
  return list;
};
