package Input;

import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

public class KeyManager implements KeyListener{
	public boolean left, right, jump, ability;
	private boolean[] keys;
	public KeyManager(){
		keys = new boolean[256];
	}
	public void tick(){
		left = keys[KeyEvent.VK_LEFT];
		right = keys[KeyEvent.VK_RIGHT];
		jump = keys[KeyEvent.VK_SPACE];
		ability = keys[KeyEvent.VK_SHIFT];
	}
	@Override
	public void keyPressed(KeyEvent e) {
		keys[e.getKeyCode()] = true;
		
	}

	@Override
	public void keyReleased(KeyEvent e) {
		keys[e.getKeyCode()] = false;
		
	}
	@Override
	public void keyTyped(KeyEvent e) {
		
		
	}
}
