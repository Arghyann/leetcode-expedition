type H2O struct {
    mu sync.Mutex
    c *sync.Cond
    h,o int
}

func NewH2O() *H2O {
	h:= &H2O{}
    h.c=sync.NewCond(&h.mu)
	return h
}

func (h *H2O) Hydrogen(releaseHydrogen func()) {
	h.mu.Lock()
    for h.h == 2 {
        h.c.Wait()

    }
    // releaseHydrogen() outputs "H". Do not change or remove this line.
	releaseHydrogen()
    h.h=h.h+1
    h.c.Broadcast()
    for h.o==1 && h.h==2{
        h.h=0
        h.o=0
        h.c.Broadcast()
    }
    h.mu.Unlock()
}

func (h *H2O) Oxygen(releaseOxygen func()) {
    h.mu.Lock()
    defer h.mu.Unlock()
    for h.o==1{
        h.c.Wait()
    }
    // releaseOxygen() outputs "H". Do not change or remove this line.
	releaseOxygen()
    h.o=h.o+1
    h.c.Broadcast()
    for h.o==1 && h.h==2{
        h.h=0
        h.o=0
        h.c.Broadcast()
    }
}