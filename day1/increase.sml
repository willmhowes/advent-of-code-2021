(* Day 01.1 - Advent of Code *)
(* Author: Will Howes *)
(* Goal: Count the number of times a depth measurement increases
         from the previous measurement. *)

(* inc : int list -> int *)
fun inc nil = 0
  | inc (l::ls) =
    if ls = nil orelse l >= (hd ls)
        then inc ls
        else 1 + inc ls;
