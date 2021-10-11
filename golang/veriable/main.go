package main

import (
	"fmt"
	"math/rand"
	"strconv"
	"strings"
	"time"
)

type Pack struct {
	a  int
	b  int
	c  int
	d  int
	e  int
	f  int64
	g  int64
	s1 string
	s2 string
	s3 string
	s4 string
	s5 string
	s6 string
	s7 string
}

func main() {
	fmt.Println("start")
	repeat := 1000000000
	p1 := genPack()
	p2 := genPack()
	pp2 := &p2

	ts1 := time.Now()
	for i := 0; i < repeat; i++ {
		p1 = assignV(p1)
	}
	fmt.Printf("time code 1: %v\n", time.Since(ts1))

	ts2 := time.Now()
	for i := 0; i < repeat; i++ {
		pp2 = assignP(pp2)
	}
	fmt.Printf("time code 2: %v\n", time.Since(ts2))

	fmt.Println("end")
}

func genLongStr() string {
	l := 100
	slic := make([]string, l)
	for i := 0; i < l; i++ {
		slic[i] = strconv.FormatInt(rand.Int63(), 10)
	}
	return strings.Join(slic, ",")
}

func genPack() Pack {
	return Pack{
		a:  1,
		b:  1,
		c:  1,
		d:  1,
		e:  1,
		f:  1,
		g:  1,
		s1: genLongStr(),
		s2: genLongStr(),
		s3: genLongStr(),
		s4: genLongStr(),
		s5: genLongStr(),
		s6: genLongStr(),
		s7: genLongStr(),
	}
}

func assignV(pack Pack) Pack {
	pack.f++
	return pack
}

func assignP(p *Pack) *Pack {
	p.f++
	return p
}
