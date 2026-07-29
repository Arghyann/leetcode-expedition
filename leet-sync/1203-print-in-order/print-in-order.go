type Foo struct {
    firstDone chan int
    secondDone chan int
}

func NewFoo() *Foo {
	return &Foo{
        firstDone:  make(chan int),
		secondDone: make(chan int),
	}
}

func (f *Foo) First(printFirst func()) {
	// Do not change this line
	printFirst()
    f.firstDone <- 1
}

func (f *Foo) Second(printSecond func()) {
    <-f.firstDone
	/// Do not change this line
	printSecond()
    f.secondDone <- 1
}

func (f *Foo) Third(printThird func()) {
	// Do not change this line
    <- f.secondDone
	printThird()
}