package Graphics;

import java.awt.image.BufferedImage;

public class Assets {
	private static final int width = 32, height = 32;
	public static BufferedImage grass, dirt, rock, brick, dashL, dashR;
	public static BufferedImage[] player_down, player_up, player_right, player_left, player_sword;
	public static BufferedImage title;
	public static BufferedImage[] play_button;
	public static void init(){
		SpriteSheet sheet = new SpriteSheet(ImageLoader.loadImage("/textures/SpriteSheet2.png"));
		
		player_down = new BufferedImage[3];
		player_up = new BufferedImage[3];
		player_right = new BufferedImage[5];
		player_left = new BufferedImage[5];
		player_sword = new BufferedImage[2];
		
		play_button = new BufferedImage[2];
		
		player_down[0] = sheet.crop(width, height, width, height);
		player_down[1] = sheet.crop(width * 2, height, width, height);
		player_down[2] = sheet.crop(0, height, width, height);
		player_up[0] = sheet.crop(width * 2, height * 3, width, height);
		player_up[1] = sheet.crop(width * 3, height * 3, width, height);
		player_up[2] = sheet.crop(width, height * 3, width, height);
		player_right[0] = sheet.crop(0, height * 2, width, height);
		player_right[1] = sheet.crop(width * 3, height, width, height);
		player_right[2] = sheet.crop(width, height * 2, width, height);
		player_right[3] = sheet.crop(width * 3, height, width, height);
		player_right[4] = sheet.crop(width * 3, height, width, height);
		player_left[0] = sheet.crop(width * 3, height * 2, width, height);
		player_left[1] = sheet.crop(width * 2, height * 2, width, height);
		player_left[2] = sheet.crop(0, height * 3, width, height);
		player_left[3] = sheet.crop(width * 2, height * 2, width, height);
		player_left[4] = sheet.crop(width * 2, height * 2, width, height);
		player_sword[0] = sheet.crop(width * 4, height * 2, width, height);
		player_sword[1] = sheet.crop(width * 5, height * 2, width, height);
		
		title = sheet.crop(width * 4, 0, width * 3, height);
		play_button[0] = sheet.crop(width * 4, height, width * 2, height);
		play_button[1] = sheet.crop(width * 6, height, width * 2, height);
		
		dirt = sheet.crop(width, 0, width, height);
		grass = sheet.crop(width * 2, 0, width, height);
		rock = sheet.crop(width * 3, 0, width, height);
		brick = sheet.crop(0, 0, width, height);
		dashL = sheet.crop(width * 5, height * 4, width, height);
		dashR = sheet.crop(width * 4, height * 4, width, height);
	}
}
