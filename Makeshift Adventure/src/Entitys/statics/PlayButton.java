package Entitys.statics;

import java.awt.Graphics;

import FirstPackage.Handler;
import Graphics.Assets;
import Tiles.Tile;

public class PlayButton extends StaticEntity{
	private int state = 0;
	
	public int getState() {
		return state;
	}

	public void setState(int state) {
		this.state = state;
	}

	public PlayButton(Handler handler, float x, float y) {
		super(handler, x, y, Tile.TILEWIDTH * 2, Tile.TILEHEIGHT);
	}

	@Override
	public void tick() {
		if(handler.getMouseManager().getMouseX() >= 256 && handler.getMouseManager().getMouseX() <= 384 && handler.getMouseManager().getMouseY() >= 320 && handler.getMouseManager().getMouseY() <= 384){
			state = 1;
		}
		else{
			state = 0;
		}
	}

	@Override
	public void render(Graphics g) {
		g.drawImage(Assets.play_button[state], (int)x, (int)y, width, height, null);
	}

	@Override
	public void die() {
		// TODO Auto-generated method stub
		
	}
}
