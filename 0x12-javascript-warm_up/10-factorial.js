#!/usr/bin/node

function factorial (ff) {
  return ff === 0 || isNaN(ff) ? 1 : ff * factorial(ff - 1);
}

console.log(factorial(Number(process.argv[2])));
