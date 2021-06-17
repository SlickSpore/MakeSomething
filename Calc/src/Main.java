import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

/*
	Program Written In 17/06/2021
	
	Lenguage: Java SE-15 

	Written By Ettore Cacccioli SlickSpore
	
	CALCULATOR
	
*/

public class Main implements ActionListener{
	JFrame f;
	JPanel p;
	JButton[] butts = new JButton[10];
	JButton[] funcs = new JButton[7];
	JTextField text;
	JLabel l;
	JLabel[] foo = new JLabel[7];
	
	String first = "";
	String second = "";
	String result = "";
	
	int operator = 0;
	
	boolean pointer = true;
	
	Main(){
		
		f = new JFrame("Calc");
		f.setSize(400,520);
		f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		f.setResizable(false);
		f.setIconImage(new ImageIcon("immagine.png").getImage());
		
		
		
		for (int i = 0; i<10; i++) {
			butts[i] = new JButton(Integer.toString(i));
			butts[i].addActionListener(this);
			butts[i].setFont(new Font("Monaco", Font.BOLD, 20));
		
		}
		for (int i = 0; i<7; i++) {
			foo[i] = new JLabel("");
		
		}		
		funcs[0] = new JButton("CE");
		funcs[1] = new JButton("+");
		funcs[2] = new JButton("-");
		funcs[3] = new JButton("/");
		funcs[4] = new JButton("*");
		funcs[5] = new JButton(".");
		funcs[6] = new JButton("=");

		
		for(int i = 0; i<6;i++) {
			funcs[i].addActionListener(this);
			funcs[i].setFont(new Font("Monaco", Font.PLAIN, 20));
		}
		
		p = new JPanel();
		p.setLayout(new GridLayout(6,5,10,10));
		p.setLocation(10, 90);
		p.setBounds(90, 90, 10, 12);
		for(int i = 0; i<10;i++) {
			p.add(butts[i]);
		}
		
		p.add(foo[0]);
		p.add(foo[1]);
		p.add(foo[2]);
		p.add(foo[3]);
		p.add(butts[1]);
		p.add(butts[2]);
		p.add(butts[3]);
		p.add(funcs[0]);

		p.add(butts[4]);
		p.add(butts[5]);
		p.add(butts[6]);
		p.add(funcs[1]);

		p.add(butts[7]);
		p.add(butts[8]);
		p.add(butts[9]);
		p.add(funcs[2]);

		p.add(funcs[5]);
		p.add(butts[0]);
		p.add(funcs[6]);
		p.add(funcs[4]);
		
		p.add(foo[4]);
		p.add(foo[5]);
		p.add(foo[6]);
		p.add(funcs[3]);
		text = new JTextField();
		text.setBounds(25, 30, 325, 40);
		text.setEditable(false);
		text.setFont(new Font("Monaco", Font.PLAIN, 20));
		f.add(text);
		f.getContentPane().add(p);
		f.setVisible(true);
	}
	public static void main(String args[]) {
		Main m = new Main(); 
		
	}
	@Override
	public void actionPerformed(ActionEvent e) {
		for (int i = 0; i<10; i++) {
			if(e.getSource()==butts[i]) {
				
				if (pointer == true) {
					first+=Integer.toString(i);
					text.setText(first);
				}
				if (pointer == false) {
					second+=Integer.toString(i);
					text.setText(second);
				}
			}
			if(e.getSource()==funcs[0]) {
				first = "";
				second="";
				result = "";
				text.setText("");
				pointer = true;
				operator = 0;
				
			}
			if(e.getSource()==funcs[1]) {
				pointer = false;
				operator = 1;
				
			}
			if(e.getSource()==funcs[2]) {
				pointer = false;
				operator = 2;
				
			}
			if(e.getSource()==funcs[3]) {
				pointer = false;
				operator = 3;
				
			}
			if(e.getSource()==funcs[4]) {
				pointer = false;
				operator = 4;
				
			}

								
			
		}
		if(e.getSource()==funcs[5]) {
			if(pointer == true) {
				first+=(".");
				text.setText(first);
			}
			if(pointer == false) {
				second.concat(".");
				text.setText(second);
			}				
			
		}
		if(e.getSource()==funcs[6]) {
			if(operator == 1) {
				result = Float.toString(Float.parseFloat(first)+Float.parseFloat(second));
				text.setText(result);
				first = "";
				second = "";
				first = result;
				
			}
			if(operator == 2) {
				result = Float.toString(Float.parseFloat(first)-Float.parseFloat(second));
				text.setText(result);
				first = "";
				second = "";
				first = result;
				
			}

			if(operator == 3) {
				result = Float.toString(Float.parseFloat(first)/Float.parseFloat(second));
				text.setText(result);
				first = "";
				second = "";
				first = result;
				
			}

			if(operator == 4) {
				result = Float.toString(Float.parseFloat(first)*Float.parseFloat(second));
				text.setText(result);
				first = "";
				second = "";
				first = result;
				
			}


		}	
	}
}
