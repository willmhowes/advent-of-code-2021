(* Day 01.1 - Advent of Code *)
(* Author: Will Howes *)
(* Goal: Count the number of times a depth measurement increases
         from the previous measurement. *)

(* ctPosDelta : int list -> int *)
fun ctPosDelta nil = 0
  | ctPosDelta (l::ls) =
    if ls = nil orelse l >= (hd ls)
        then ctPosDelta ls
        else 1 + ctPosDelta ls;
