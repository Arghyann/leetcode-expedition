type ZeroEvenOdd struct {
	n int
    odd chan int 
    even chan int
    zero chan int 
}

func NewZeroEvenOdd(n int) *ZeroEvenOdd {
	zeo := &ZeroEvenOdd{
		n : n,
        zero : make(chan int),
        even : make(chan int),
        odd : make(chan int),
	}
    
	return zeo
}

func (z *ZeroEvenOdd) Zero(printNumber func(int)) {
    for i:=1; i<=z.n;i++{
        if i!=1{
            <-z.zero
        }
        printNumber(0)
        if i % 2 == 0{
            z.even <- i
        }else{
        
            z.odd <- i
        }
    }
    close(z.even)
    close(z.odd)

}

func (z *ZeroEvenOdd) Even(printNumber func(int)) {
    for n := range z.even{
        printNumber(n)
        if n == z.n{
            return
        }
        z.zero<-0
    } 
}

func (z *ZeroEvenOdd) Odd(printNumber func(int)) {
    for n := range z.odd{
        printNumber(n)
        if n == z.n{
            return
        }
        z.zero<-0
    }
}