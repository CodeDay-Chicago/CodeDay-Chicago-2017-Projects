package Entitys.creatures;

import Entitys.Entity;
import FirstPackage.Game;
import FirstPackage.Handler;
import Tiles.Tile;

public abstract class Creatures extends Entity{

	public static final float DEFAULT_YSPEED = 4.0f, DEFAULT_SPEED = 3.0f;
	public static final int DEFAULT_CREATURE_WIDTH = 64;
	public static final int DEFAULT_CREATURE_HEIGHT = 64;
	
	
	protected float speed, ySpeed;
	protected float xMove, yMove;
	
	public Creatures(Handler handler, float x, float y, int width, int height) {
		super(handler, x, y, width, height);
	
		speed = DEFAULT_SPEED;
		ySpeed = DEFAULT_YSPEED;
		xMove = 0;
		yMove = 0;
	}
	public void move(){
		if(xMove > 0){//Moving Right
			int tx = (int)(x + xMove + bounds.x + bounds.width) / Tile.TILEWIDTH;
			if(!collisionWithTile(tx, (int) (y + bounds.y) / Tile.TILEHEIGHT) && !collisionWithTile(tx, (int) (y + bounds.y + bounds.height) / Tile.TILEHEIGHT)){
				x += xMove;
			}
			else{
				x = tx * Tile.TILEWIDTH - bounds.x - bounds.width - 1;
			}
		}
		else if(xMove < 0){//Moving Left
			int tx = (int)(x + xMove + bounds.x) / Tile.TILEWIDTH;
			if(!collisionWithTile(tx, (int) (y + bounds.y) / Tile.TILEHEIGHT) && !collisionWithTile(tx, (int) (y + bounds.y + bounds.height) / Tile.TILEHEIGHT)){
				x += xMove;
			}
			else{
				x = tx * Tile.TILEWIDTH + Tile.TILEWIDTH - bounds.x;
			}
		}
		if(yMove < 0){
			int ty = (int)(y + yMove + bounds.y) / Tile.TILEHEIGHT;
			if(!collisionWithTile(ty, (int) (x + bounds.x) / Tile.TILEWIDTH) && !collisionWithTile(ty, (int) (y + bounds.y + bounds.width) / Tile.TILEWIDTH)){
				y += yMove;
			}
			else{
				y = ty * Tile.TILEWIDTH + Tile.TILEHEIGHT - bounds.y;
			}
			
		}
		else if(yMove > 0){//Moving Right
			int ty = (int)(y + yMove + bounds.y + bounds.height) / Tile.TILEHEIGHT;
			if(!collisionWithTile(ty, (int) (x + bounds.x) / Tile.TILEWIDTH) && !collisionWithTile(ty, (int) (x + bounds.x + bounds.width) / Tile.TILEWIDTH)){
				y += yMove;
			}
			else{
				y = ty * Tile.TILEHEIGHT - bounds.y - bounds.height - 1;
			}
		}
	}
	public void moveX(){
		if(xMove > 0){//Moving Right
			int tx = (int)(x + xMove + bounds.x + bounds.width) / Tile.TILEWIDTH;
			if(!collisionWithTile(tx, (int) (y + bounds.y) / Tile.TILEHEIGHT) && !collisionWithTile(tx, (int) (y + bounds.y + bounds.height) / Tile.TILEHEIGHT)){
				x += xMove;
			}
			else{
				x = tx * Tile.TILEWIDTH - bounds.x - bounds.width - 1;
			}
		}
		else if(xMove < 0){//Moving Left
			int tx = (int)(x + xMove + bounds.x) / Tile.TILEWIDTH;
			if(!collisionWithTile(tx, (int) (y + bounds.y) / Tile.TILEHEIGHT) && !collisionWithTile(tx, (int) (y + bounds.y + bounds.height) / Tile.TILEHEIGHT)){
				x += xMove;
			}
			else{
				x = tx * Tile.TILEWIDTH + Tile.TILEWIDTH - bounds.x;
			}
		}
		if(yMove < 0){
			int ty = (int)(y + yMove + bounds.y) / Tile.TILEHEIGHT;
			if(!collisionWithTile(ty, (int) (x + bounds.x) / Tile.TILEWIDTH) && !collisionWithTile(ty, (int) (y + bounds.y + bounds.width) / Tile.TILEWIDTH)){
				y += yMove;
			}
			else{
				y = ty * Tile.TILEWIDTH + Tile.TILEHEIGHT - bounds.y;
			}
			
		}
		else if(yMove > 0){//Moving Right
			int ty = (int)(y + yMove + bounds.y + bounds.height) / Tile.TILEHEIGHT;
			if(!collisionWithTile(ty, (int) (x + bounds.x) / Tile.TILEWIDTH) && !collisionWithTile(ty, (int) (x + bounds.x + bounds.width) / Tile.TILEWIDTH)){
				y += yMove;
			}
			else{
				y = ty * Tile.TILEHEIGHT - bounds.y - bounds.height - 1;
			}
		}
	}
	protected boolean collisionWithTile(int x, int y){
		return handler.getWorld().getTile(x, y).isSolid();
	}
	//Getters & Setters
	public float getxMove() {
		return xMove;
	}

	public void setxMove(float xMove) {
		this.xMove = xMove;
	}

	public float getyMove() {
		return yMove;
	}

	public void setyMove(float yMove) {
		this.yMove = yMove;
	}

	public int getHealth() {
		return health;
	}

	public void setHealth(int health) {
		this.health = health;
	}

	public float getSpeed() {
		return speed;
	}

	public void setSpeed(float speed) {
		this.speed = speed;
	}
	//GRAVITY
	public void gravity(){
		if(y < 448){
			y += 4;
		}
	}
}
