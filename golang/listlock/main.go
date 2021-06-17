package main

import (
	"fmt"
	"strconv"
	"strings"
	"sync"
	"time"
)

const (
	//workerCount int = 10
	wrapperSize int = 5
)

var holder []string
var lock sync.Mutex

func main() {
	fmt.Println("starting")

	ch := make(chan int, 1000)

	go func() {
		for n := range ch {
			go func(num int) {
				ns := strconv.Itoa(num)
				lock.Lock()
				holder = append(holder, ns)
				if len(holder) >= wrapperSize {
					go func(s []string) {
						fmt.Printf("holder is ready to refresh: %s\n", strings.Join(s, ","))
					}(holder)
					holder = make([]string, 0, 5)
				}
				lock.Unlock()
			}(n)
		}
	}()

	emit(ch)
	for len(ch) != 0 {
		fmt.Printf("chan size is %v\n", len(ch))
		if len(ch) == 0 {
			return
		}
		time.Sleep(time.Millisecond * 100)
	}
}

func emit(ch chan int) {
	for i := 0; i < 100; i++ {
		ch <- i
	}
	fmt.Printf("emit finished\n")
}
