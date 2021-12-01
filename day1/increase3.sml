(* Day 01.2 - Advent of Code *)
(* Author: Will Howes *)
(* Goal: Consider sums of a three-measurement sliding window.
         Count the number of times the sum of measurements in
         this sliding window increases from the previous sum *)

(* ctWindowIncreaseHelper : int list -> int *)
fun ctWindowIncreaseHelper nil = 0
  | ctWindowIncreaseHelper (l::ls) =
    if tl (tl ls) = nil
        then 0
    else if l >= hd (tl (tl ls))
        then ctWindowIncreaseHelper ls
        else 1 + ctWindowIncreaseHelper ls;

(* ctWindowIncrease : int list -> int *)
fun ctWindowIncrease nil = 0
  | ctWindowIncrease (l::ls) =
    if ls = nil orelse tl ls = nil
                orelse tl (tl ls) = nil
        then 0
        else ctWindowIncreaseHelper (l::ls);
