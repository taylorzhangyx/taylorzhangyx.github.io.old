package main

import (
	"context"
	"fmt"
	"strconv"
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
	ctx := context.Background()
	ctx, cancle := context.WithTimeout(ctx, time.Millisecond)
	defer cancle()
	st := time.Now()
	defer func() {
		et := time.Now()
		fmt.Printf("time cost %v", et.Sub(st))
	}()

	ch := make(chan int, 1000)
	donech := make(chan bool)

	go func() {
		var wg sync.WaitGroup
		for n := range ch {
			//go func(num int) {
			//ns := strconv.Itoa(num)
			ns := strconv.Itoa(n)
			lock.Lock()
			holder = append(holder, ns)
			if len(holder) >= wrapperSize {
				wg.Add(1)
				go func(s []string) {
					//fmt.Printf("holder is ready to refresh: %s\n", strings.Join(s, ","))
					time.Sleep(time.Millisecond)
					wg.Done()
				}(holder)
				holder = make([]string, 0, wrapperSize)
			}
			lock.Unlock()
			//}(n)
		}
		wg.Wait()
		donech <- true
		close(donech)
	}()

	go emit(ch)
	for {
		select {
		case b := <-donech:
			fmt.Printf("done channel get %v\n", b)
			return
		case ctout := <-ctx.Done():
			fmt.Printf("timeout [%v] [%v]", ctx.Err(), ctout)
			return
		}
	}
}

func emit(ch chan int) {
	for i := 0; i < 3000000; i++ {
		ch <- i
	}
	close(ch)
	fmt.Printf("emit finished\n")
}
