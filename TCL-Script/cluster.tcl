set sel "name S"
set a [atomselect top "$sel"]
set b [atomselect top "name O3 H5 O5 H O and within 6.0 of $sel"]
set k 0
set matrix(0,0) 0
for {set i 0} {$i<=1} {incr i} {
     $a frame $i
     $a update
     $b frame $i
     $b update
     set selist [$a list]
     set n [$a num]
     set pairs [$b num]
for { set x 0 } { $x <= [expr $n-2] } { incr x } {
	  for { set y [expr $x+1] } { $y <= [expr $n-1] } { incr y } {
	        set a [lindex $selist $x]
	        set b [lindex $selist $y]
	        set c [atomselect top "index $a"] 
	        set P1 [measure center "$c"]
	        set d [atomselect top "index $b"]
	        set P2 [measure center "$d"]
	        set VA [vecsub $P1 $P2]
	        set DISTA [veclength $VA]
	        set matrix($x,$y) $DISTA;#将DISTA赋给矩阵matrix
	        set matrix($y,0) $y;#将matrix($y,0)定义为团簇名称
	       }
}


set min_distance 0
set clusternum $n
while {$min_distance<=6.5} {
set flag 1
for { set x 0 } { $x <= [expr $n-2] } { incr x } {
	  for { set y [expr $x+1] } { $y <= [expr $n-1] } { incr y } {
	        if { $matrix($y,0) == $matrix($x,0) } {
	            continue;#是同一个团簇 
            } elseif { $flag == 1 } {
	                   set min_distance $matrix($x,$y)
	                   set cluster_1 $x
	                   set cluster_2 $y
	                   set flag 0
	                   continue;#set initial value
            } 
            if { $matrix($x,$y)<$min_distance } {
	        set min_distance $matrix($x,$y)
	        set cluster_1 $x
	        set cluster_2 $y
	        }
      }
    }
      if { $min_distance>=6.5 } break
	  set buffer $matrix($cluster_2,0)
	  incr clusternum -1
	  for { set z 0 } { $z <= [expr $n-1] } { incr z } {
	      if { $matrix($z,0) == $buffer } {
	           set matrix($z,0) $matrix($cluster_1,0);#合并两个团簇
	         }
	      }
} 
	puts $clusternum
	set k [expr $k+$clusternum]
	puts $k
}

  
