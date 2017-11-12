package States;

import java.awt.Graphics;
import FirstPackage.Handler;
import Worlds.World;

public class GameState extends State{
	private World world;
	
	public GameState(Handler handler){
		super(handler);
		world = new World(handler, "res/worlds/sideworld.txt");
		handler.setWorld(world);
		
		handler.getGameCamera().move(0, 0);
	}
	@Override
	public void tick() {
		world.tick();
	}

	@Override
	public void render(Graphics g) {
		world.render(g);
	}

}
