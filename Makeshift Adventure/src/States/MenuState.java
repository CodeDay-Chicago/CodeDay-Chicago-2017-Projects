package States;

import java.awt.Color;
import java.awt.Graphics;
import FirstPackage.Handler;
import Graphics.Assets;
import Tiles.Tile;
import Utils.Utils;
import Entitys.statics.PlayButton;
import Entitys.statics.Title;

public class MenuState extends State{
	
		private int[][] tiles;
		private int width, height;
		public PlayButton playbutton;
		public Title title;
		public MenuState(Handler handler){
			super(handler);
			loadMenu("res/worlds/menuWorld.txt");
			playbutton = new PlayButton(handler, 256, 320);
			title = new Title(handler, 128, 64);
		}
		@Override
		public void tick() {
			playbutton.tick();
			
			if(playbutton.getState() == 1 && handler.getMouseManager().isLeftPressed() == true){
				State.setState(handler.getGame().gameState);
			}
		}

		@Override
		public void render(Graphics g) {
			for(int y = 0; y < height; y++){
				for(int x = 0; x < width; x++){
					getTile(x,y).render(g, x * Tile.TILEWIDTH, y * Tile.TILEHEIGHT);;
				}
			}
			playbutton.render(g);
			title.render(g);
		}
		public Tile getTile(int x, int y){
			Tile t = Tile.tiles[tiles[x][y]];
			if(t== null){
				return Tile.dirtTile;
			}
			return t;
		}
		public void loadMenu(String path){
			String file = Utils.loadFileAsString(path);
			String[] tokens = file.split("\\s+");
			width = Utils.parseInt(tokens[0]);
			height = Utils.parseInt(tokens[1]);
			tiles = new int[width][height];
			for(int y = 0; y < height; y++){
				for(int x = 0; x < width; x++){
					tiles[x][y] = Utils.parseInt(tokens[(x + y * width) + 2]);
				}
			}
		}
			
	}
