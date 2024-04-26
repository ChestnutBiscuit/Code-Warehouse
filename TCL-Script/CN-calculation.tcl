set result [open result.txt w]
set sel "name OX"
set selin [atomselect top "$sel"]
set sel1 [atomselect top "name CB1 CB2 CB3 CB4 FB1 FB2 FB3 FB4 C1 C2 C3 C4 C5 F1 F2 F3 F4 F5 and within 6 of $sel"]
set sel2 [atomselect top "name S O3 H5 O5 H O and within 6 of $sel"]
set fps1 0
set fps2 400
set x 0
set y 0
for {set i $fps1} {$i<=$fps2} {incr i} {
$selin frame $i
$selin update
$sel1 frame $i
$sel1 update
$sel2 frame $i
$sel2 update
set a [$sel1 num]
set b [$sel2 num]
puts $result "$a"
puts $result "$b"
set x [expr $x+$a]
set y [expr $y+$b]
}
set cn1 [expr $x/[expr ($fps2-$fps1)]]
set cn2 [expr $y/[expr ($fps2-$fps1)]]
puts $result "$cn1"
puts $result "$cn2"
close $result