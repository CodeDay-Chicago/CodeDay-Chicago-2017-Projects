package Entitys.statics;

import java.awt.Graphics;

import FirstPackage.Handler;
import Graphics.Assets;
import Tiles.Tile;

public class Title extends StaticEntity{

	public Title(Handler handler, float x, float y) {
		super(handler, x, y, Tile.TILEWIDTH * 6, Tile.TILEHEIGHT * 2);
	}

	@Override
	public void die() {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void tick() {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void render(Graphics g) {
		g.drawImage(Assets.title, (int)x, (int)y, width, height, null);
	}
	
}
