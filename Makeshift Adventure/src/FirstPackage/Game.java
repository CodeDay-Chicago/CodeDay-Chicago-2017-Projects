package FirstPackage;

import java.awt.Graphics;
import java.awt.image.BufferStrategy;
import java.awt.image.BufferedImage;

import Display.Display;
import Graphics.Assets;
import Graphics.GameCamera;
import Graphics.ImageLoader;
import Graphics.SpriteSheet;
import Input.KeyManager;
import Input.MouseManager;
import States.GameState;
import States.MenuState;
import States.State;

public class Game implements Runnable{
	private Display display;
	private boolean running = false;
	private int width, height;
	public String title;
	
	private Thread thread;
	
	private BufferStrategy bs;
	private Graphics g;
	
	//States
	public State gameState;
	public State menuState;
	
	//Input
	private KeyManager keyManager;
	private MouseManager mouseManager;
	//Game Camera
	private GameCamera gameCamera;
	
	//Handler
	private Handler handler;
	public Game(String title, int width, int height){
		this.width = width;
		this.height = height;
		this.title = title;
		keyManager = new KeyManager();
		mouseManager = new MouseManager();
	}
	private void init(){
		display = new Display(title, width, height);
		display.getframe().addKeyListener(keyManager);
		display.getframe().addMouseListener(mouseManager);
		display.getframe().addMouseMotionListener(mouseManager);
		display.getCanvas().addMouseListener(mouseManager);
		display.getCanvas().addMouseMotionListener(mouseManager);
		Assets.init();
		
		handler = new Handler(this);
		gameCamera = new GameCamera(handler, 0, 0);
		
		
		gameState = new GameState(handler);
		menuState = new MenuState(handler);
		State.setState(menuState);
	}
	
	private void tick(){
		keyManager.tick();
		if(State.getState() != null){
			State.getState().tick();
			
		}
	}
	private void render(){
		bs = display.getCanvas().getBufferStrategy();
		if(bs == null){
			display.getCanvas().createBufferStrategy(3);
			return;
		}
		g = bs.getDrawGraphics();
		//Clear Screen
		g.clearRect(0, 0, width, height);
		//Draw Here
		if(State.getState() != null){
			State.getState().render(g);
		}
		
		//End Drawing
		bs.show();
		g.dispose();
	}
	public void run(){
		init();
		
		int fps = 60;
		double timePerTick = 1000000000 / fps;
		double delta = 0;
		long now;
		long lastTime = System.nanoTime();
		long timer = 0;
		int ticks = 0;
		
		while(running){
			now = System.nanoTime();
			delta += (now - lastTime) / timePerTick;
			timer = now - lastTime;
			lastTime = now;
			if(delta >= 1){
				tick();
				render();
				ticks++;
				delta--;
			}
		}
		stop();
	}
	public KeyManager getKeyManager(){
		return keyManager;
	}
	public MouseManager getMouseManager(){
		return mouseManager;
	}
	public GameCamera getGameCamera(){
		return gameCamera;
	}
	public int getWidth(){
		return width;
	}
	public int getHeight(){
		return height;
	}
	public synchronized void start(){
		if(running)
			return;
		running = true;
		thread = new Thread(this);
		thread.start();
	}
	public synchronized void stop(){
		if(!running)
			return;
		running = false;
		try {
			thread.join();
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	}
}
