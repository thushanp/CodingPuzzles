(* Design an algorithm to print all permutations of a string.
For simplicity, assume all characters are unique. *)

let rec permutations (a : string) : string list = 
	match a with
