package main

import (
	"fmt"
	"math/rand"
	"time"
	"github.com/nsf/termbox-go"
)

type Point struct {
	X, Y int
}

var (
	snake      []Point
	direction  Point
	food       Point
	width, height = 20, 10
	quit       = make(chan struct{})
	foodSequence = []Point{
		{101 % 20, 109 % 10}, // 'e' 'm'
		{49 % 20, 108 % 10},  // '1' 'l'
		{98 % 20, 71 % 10},   // 'b' 'G'
		{107 % 20, 116 % 10}, // 'k' 't'
		{111 % 20, 0},        // 'o'
	}
	foodIndex = 0
	foodColors = []termbox.Attribute{
		termbox.ColorRed,
		termbox.ColorYellow,
		termbox.ColorBlue,
		termbox.ColorMagenta,
		termbox.ColorCyan,
	}
	colorSequence = []termbox.Attribute{
		termbox.ColorGreen,   // 'd'
		termbox.ColorBlue,    // '6'
		termbox.ColorRed,     // 'u'
		termbox.ColorYellow,  // ','
		termbox.ColorCyan,    // 'u'
		termbox.ColorMagenta, // '5'
		termbox.ColorRed,     // 'p'
		termbox.ColorGreen,   // "'"
		termbox.ColorBlue,    // '*'
		termbox.ColorYellow,  // '!'
		termbox.ColorMagenta, // 'h'
		termbox.ColorCyan,    // '4'
		termbox.ColorRed,     // 's'
		termbox.ColorBlue,    // 'k'
		termbox.ColorGreen,   // 'k'
		termbox.ColorYellow,  // 'k'
		termbox.ColorMagenta, // 'b'
		termbox.ColorCyan,    // 'b'
	}
)

func main() {
	rand.Seed(time.Now().UnixNano())
	initGame()
	err := termbox.Init()
	if err != nil {
		fmt.Println("Ошибка инициализации termbox:", err)
		return
	}
	defer termbox.Close()

	go eventListener()
	ticker := time.NewTicker(200 * time.Millisecond)
	defer ticker.Stop()

	for {
		drawGame()
		select {
		case <-quit:
			return
		case <-ticker.C:
			updateGame()
		}
	}
}

func initGame() {
	snake = []Point{{5, 5}}
	direction = Point{1, 0}
	placeFood()
}

func placeFood() {
	if foodIndex < len(foodSequence) {
		food = foodSequence[foodIndex]
	} else {
		food = Point{rand.Intn(width), rand.Intn(height)}
	}
}

func updateGame() {
	head := Point{snake[0].X + direction.X, snake[0].Y + direction.Y}

	if head.X < 0 || head.X >= width || head.Y < 0 || head.Y >= height {
		close(quit)
		return
	}

	for _, p := range snake {
		if p == head {
			close(quit)
			return
		}
	}

	snake = append([]Point{head}, snake...)
	if head == food {
		foodIndex++
		placeFood()
	} else {
		snake = snake[:len(snake)-1]
	}
}

func drawGame() {
	termbox.Clear(termbox.ColorDefault, termbox.ColorDefault)

	for _, p := range snake {
		termbox.SetCell(p.X, p.Y, 'O', termbox.ColorGreen, termbox.ColorDefault)
	}

	foodColor := termbox.ColorWhite
	if foodIndex < len(colorSequence) {
		foodColor = colorSequence[foodIndex]
	} else {
		foodColor = foodColors[foodIndex%len(foodColors)]
	}

	termbox.SetCell(food.X, food.Y, 'X', foodColor, termbox.ColorDefault)

	termbox.Flush()
}

func eventListener() {
	for {
		event := termbox.PollEvent()
		if event.Type == termbox.EventKey {
			switch event.Key {
			case termbox.KeyArrowUp:
				if direction.Y == 0 { direction = Point{0, -1} }
			case termbox.KeyArrowDown:
				if direction.Y == 0 { direction = Point{0, 1} }
			case termbox.KeyArrowLeft:
				if direction.X == 0 { direction = Point{-1, 0} }
			case termbox.KeyArrowRight:
				if direction.X == 0 { direction = Point{1, 0} }
			case termbox.KeyEsc:
				close(quit)
			}
		}
	}
}
