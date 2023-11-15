#!/usr/bin/node

const args = process.argv.slice(2).map(Number).sort((a, b) => b - a);

if (args.length <= 1) {
	console.log(0);
}
else {
	let max = args[0];
	for(let y = 1; y < args.length; y++){
		if (args[y] !== max) {
			console.log(args[y]);
			break
		}
	}
}
