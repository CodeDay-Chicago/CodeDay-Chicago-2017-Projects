package Graphics;

import java.awt.image.BufferedImage;

public class Animation {
	private int speed, index;
	private long lastTime, timer;
	private BufferedImage[] frames;
	
	public Animation(int speed, BufferedImage[] frames){
		this.speed = speed;
		this.frames = frames;
		index = 0;
		timer = 0;
		lastTime = System.currentTimeMillis();
	}
	
	public void tick(){
		timer += System.currentTimeMillis() - lastTime;
		lastTime = System.currentTimeMillis();
		
		if(timer > speed){
			index++;
			timer = 0;
			if(index >= frames.length-1){
				index = 0;
			}
		}
	}
	
	public BufferedImage getCurrentFrame(){
		return frames[index];
	}
	public BufferedImage getStandingHorizontalFrame(){
		return frames[4];
	}
	public BufferedImage getStandingVerticalFrame(){
		return frames[2];
	}
	public BufferedImage getSecondAttackFrame(){
		return frames[1];
	}
}
