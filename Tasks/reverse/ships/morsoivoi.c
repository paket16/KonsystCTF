#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <locale.h>

#define SIZE 5
#define SHIP_COUNT 3

char player_board[SIZE][SIZE];
char enemy_board[SIZE][SIZE];
char enemy_hidden[SIZE][SIZE];

void init_boards(char board[SIZE][SIZE]) {
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            board[i][j] = '~';
        }
    }
}

void print_board(char board[SIZE][SIZE]) {
    printf("  0 1 2 3 4\n");
    for (int i = 0; i < SIZE; i++) {
        printf("%d ", i);
        for (int j = 0; j < SIZE; j++) {
            printf("%c ", board[i][j]);
        }
        printf("\n");
    }
}

void place_ships(char board[SIZE][SIZE]) {
    int placed = 0;
    while (placed < SHIP_COUNT) {
        int x = rand() % SIZE;
        int y = rand() % SIZE;
        if (board[x][y] == '~') {
            board[x][y] = 'S';
            placed++;
        }
    }
}

int attack(char board[SIZE][SIZE], int x, int y) {
    if (board[x][y] == 'S') {
        board[x][y] = 'X';
        return 1;
    } else if (board[x][y] == '~') {
        board[x][y] = 'O';
        return 0;
    }
    return -1;
}

void print_flag() {
    printf("EEEEEEEEEeEEeeeEEEEEEEEEEeeEeEeEEEEEEEEEEeEeeEEeEEEEEEEEEeeEEeeeEEEEEEEEEeEEeeeEEEEEEEEEEeeEeeEeEEEEEEEEEeEEeeEeEEEEEEEEEeeEEeeeEEEEEEEEEeEEeeeEEEEEEEEEEeeEeEeEEEEEEEEEEeEEEeEeEEEEEEEEEeeEEeeeEEEEEEEEEeEEeeeEEEEEEEEEEeeEeEeEEEEEEEEEEeeEEEeeEEEEEEEEEeeEEeeeEEEEEEEEEeEEeeeEEEEEEEEEEEeeEEeEEEEEEEEEEeEEeEEeEEEEEEEEEeeEEeeeEEEEEEEEEeEEeeeEEEEEEEEEEeEEEeeeEEEEEEEEEeEeEEEeEEEEEEEEEeeEEeeeEEEEEEEEEeEEeeeEEEEEEEEEEeEEEeeeEEEEEEEEEeEeeEEeEEEEEEEEEeeEEeeeEEEEEEEEEeEEeeeEEEEEEEEEEeEeEeEEEEEEEEEEEeEEeEEeEEEEEEEEEeeEEeeeEEEEEEEEEeEEeeeEEEEEEEEEEeEeEeEEEEEEEEEEEeEEeeEeEEEEEEEEEeeEEeeeEEEEEEEEEeEEeeeEEEEEEEEEEeEEEeeeEEEEEEEEEeEEeEEeEEEEEEEEEeeEEeeeEEEEEEEEEeEEeeeEEEEEEEEEEeEEEeeeEEEEEEEEEeEeeEEeEEEEEEEEEeeEEeeeEEEEEEEEEeEEeeeEEEEEEEEEEeEEEeEEEEEEEEEEEeeEeEeeEEEEEEEEEeeEEeeeEEEEEEEEEeEEeeeEEEEEEEEEEeEeEeeeEEEEEEEEEeEeeEEeEEEEEEEEEeeEEeeeEEEEEEEEEeEEeeeEEEEEEEEEEeEeEeEEEEEEEEEEEeEeeEEeEEEEEEEEEeeEEeeeEEEEEEEEEeEEeeeEEEEEEEEEEeEEEeeeEEEEEEEEEeEeeEEeEEEEEEEEEeeEEeeeEEEEEEEEEeEEeeeEEEEEEEEEEeEEEeEEEEEEEEEEEeeEeEeeEEEEEEEEEeeEEeeeEEEEEEEEEeEEeeeEEEEEEEEEEEeeEEeEEEEEEEEEEeEeEEEeEEEEEEEEEeeEEeeeEEEEEEEEEeEEeeEeEEEEEEEEEeEEEeeeEEEEEEEEEeEeEEEeEEEEEEEEEeeEEeeeEEEEEEEEEeEEeeEeEEEEEEEEEeEEEeeeEEEEEEEEEeEEEeEeEEEEEEEEEEeeeeEe");
}

int main() {
    setlocale(LC_ALL, "");
    srand(time(NULL));
    init_boards(player_board);
    init_boards(enemy_board);
    init_boards(enemy_hidden);

    place_ships(player_board);
    place_ships(enemy_board);

    int player_ships = SHIP_COUNT;
    int enemy_ships = SHIP_COUNT;
    int x, y;

    while (player_ships > 0 && enemy_ships > 0) {
        printf("Your board:\n");
        print_board(player_board);
        printf("Enemy board:\n");
        print_board(enemy_hidden);

        printf("Enter attack coordinates (x y): ");
        scanf("%d %d", &x, &y);
        if (attack(enemy_board, x, y) == 1) {
            enemy_hidden[x][y] = 'X';
            enemy_ships--;
            printf("Hit!\n");
        } else {
            enemy_hidden[x][y] = 'O';
            printf("Miss.\n");
        }

        x = rand() % SIZE;
        y = rand() % SIZE;
        if (attack(player_board, x, y) == 1) {
            player_ships--;
            printf("Enemy hit at (%d, %d)!\n", x, y);
        } else {
            printf("Enemy missed at (%d, %d).\n", x, y);
        }
    }

    if (player_ships > 0) {
        printf("You won!\n");
    } else {
        printf("You lost.\n");
    }
    return 0;
}
