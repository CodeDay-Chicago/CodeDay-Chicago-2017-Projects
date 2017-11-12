package Entitys.creatures;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.Rectangle;
import java.awt.image.BufferedImage;

import Entitys.Entity;
import FirstPackage.Handler;
import Graphics.Animation;
import Graphics.Assets;
import Tiles.Tile;

public class Player extends Creatures{
	//Animations
	private Animation animDown;
	private Animation animUp;
	private Animation animRight;
	private Animation animLeft;
	//Jump timer
	private boolean onGround = true;
	private boolean pastMid = false;
	private boolean dashing = false;
	public int lastDirection = 4;
	private int groundheight = (int) (y + bounds.height);
	private long dashStart = 0;
	
	public Player(Handler handler, float x, float y) {
		super(handler, x, y, Creatures.DEFAULT_CREATURE_WIDTH, Creatures.DEFAULT_CREATURE_HEIGHT);
		
		bounds.x = 18;
		bounds.y = 23;
		bounds.width = 28;
		bounds.height = 31;
		
		//Animations
		animDown = new Animation(500, Assets.player_down);
		animUp = new Animation(500, Assets.player_up);
		animRight = new Animation(500, Assets.player_right);
		animLeft = new Animation(500, Assets.player_left);
	}

	@Override
	public void tick() {
		//Animation
		animDown.tick();
		animUp.tick();
		animRight.tick();
		animLeft.tick();
		//Movement
		getInput();
		move();
		handler.getGameCamera().centerOnEntity(this);
	}
	private void getInput(){
		xMove = 0;
		yMove = 0;
		if (handler.getKeyManager().left) {
			xMove = -speed;
			lastDirection = 3;
		}
		
		if (handler.getKeyManager().right) {
			xMove = speed;
			lastDirection = 4;
		}
		if(onGround && handler.getKeyManager().jump){
			onGround = false;
		}
		if(!onGround){
			jump();
		}
		if(handler.getKeyManager().ability){
			dashing = true;
		}
		if(dashing){
			ability(0);
		}
		
	}
	@Override
	public void render(Graphics g) {
		g.drawImage(getCurrentAnimationFrame(), (int)(x - handler.getGameCamera().getxOffset()), (int)(y - handler.getGameCamera().getyOffset()), width, height, null);
	}
	private BufferedImage getCurrentAnimationFrame(){
		if(dashing && lastDirection == 4){
			return Assets.dashL;
		}
		if(dashing && lastDirection == 3){
			return Assets.dashR;
		}
	    if(xMove < 0){
			return animLeft.getCurrentFrame();
		}
		else if(xMove > 0){
			return animRight.getCurrentFrame();
		}
		else if(yMove < 0){
			return animUp.getCurrentFrame();
		}
		else if(yMove > 0){
			return animDown.getCurrentFrame();
		}
		else{
			if(lastDirection == 1){
				return animUp.getStandingVerticalFrame();
			}
			else if(lastDirection == 2){
				return animDown.getStandingVerticalFrame();
			}
			else if(lastDirection == 3){
				return animLeft.getStandingHorizontalFrame();
			}
			else if (lastDirection == 4){
				return animRight.getStandingHorizontalFrame();
			}
			else{
				return animRight.getStandingHorizontalFrame();
			}
		}
	}
	public void ability(int ability){
		
		if(ability == 0 && System.currentTimeMillis() >= dashStart + 500){
			dashStart = System.currentTimeMillis();
			if(lastDirection == 4){
				int tx = (int)(x + xMove + bounds.x) / Tile.TILEWIDTH;
				if(!collisionWithTile(tx, (int) (y + bounds.y) / Tile.TILEHEIGHT) && !collisionWithTile(tx, (int) (y + bounds.y + bounds.height) / Tile.TILEHEIGHT)){
					x += 192;
				}
				else{
					
				}
			}
			else if(lastDirection == 3){
				int tx = (int)(x + xMove + bounds.x) / Tile.TILEWIDTH;
				if(!collisionWithTile(tx, (int) (y + bounds.y) / Tile.TILEHEIGHT) && !collisionWithTile(tx, (int) (y + bounds.y + bounds.height) / Tile.TILEHEIGHT)){
					x -= 192;
				}
				else{
					
				}
				
			}
			dashing = false;
			
		}
		else if(ability == 1){
			
		}
	}
	public void jump(){
		
		
		if(pastMid == false){
			if(y == groundheight - 96){
				pastMid = true;
			}
			else{
				y -= ySpeed;
			}
		}
		else if(pastMid){
			int ty = (int) (y + yMove + bounds.y + bounds.height) / Tile.TILEHEIGHT;
			if(!collisionWithTile((int) (x + bounds.x) / Tile.TILEWIDTH, ty) && !collisionWithTile((int) (x + bounds.x + bounds.width) / Tile.TILEWIDTH, ty)){
				y += ySpeed;
			}
			else{
				y = ty * Tile.TILEHEIGHT - bounds.y - bounds.height - 4;
				pastMid = false;
				onGround = true;
				groundheight = (int) (y - 32);
			}
			
		}
		else{
			System.out.println("That's not supposed to happen");
		}
		/*if(!pastMid){
			int ty = (int)(y + yMove + bounds.y) / Tile.TILEHEIGHT;
			if(!collisionWithTile(ty, (int) (x + bounds.x) / Tile.TILEWIDTH) && !collisionWithTile(ty, (int) (y + bounds.y + bounds.width) / Tile.TILEWIDTH)){
				y += yMove;
			}
			else{
				y = ty * Tile.TILEWIDTH + Tile.TILEHEIGHT - bounds.y;
			}
			
		}
		else if(pastMid){
			int ty = (int)(y + yMove + bounds.y + bounds.height) / Tile.TILEHEIGHT;
			if(!collisionWithTile(ty, (int) (x + bounds.x) / Tile.TILEWIDTH) && !collisionWithTile(ty, (int) (x + bounds.x + bounds.width) / Tile.TILEWIDTH)){
				y += yMove;
			}
			else{
				y = ty * Tile.TILEHEIGHT - bounds.y - bounds.height - 1;
			}
		}*/
		
	}
	@Override
	public void die() {
		System.out.println("Great Job Buddy.");
	}
}
