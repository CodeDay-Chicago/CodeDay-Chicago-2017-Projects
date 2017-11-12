package FirstPackage;

import Display.Display;

public class Launcher {
	public static void main(String[] args){
		Game game = new Game("Makeshift Adventure", 640, 640);
		game.start();
	}
}
