package Tiles;

import Graphics.Assets;

public class TreeTile extends Tile{

	public TreeTile(int id) {
		super(Assets.brick, id);
		
	}
	@Override
	public boolean isSolid(){
		return true;
	}
}
