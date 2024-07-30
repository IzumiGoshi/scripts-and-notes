      /*
		  NOTE: 
		    To rotate textures correctly you have to use DrawTexturePro
		    source rect controls which part of the texture are drawn.
			the simple case is the entire texture
		    dst rect is the position and size.
		    player_size half is passed at the origin, placing it at the center.
		    also drawTexture takes in degrees instead of radians...
	    */
	    Rectangle src_rec = { 0.0, 0.0, player_size.x, player_size.y };
	    Rectangle dst_rec = { player_pos.x, player_pos.y, player_size.x, player_size.y };
	    DrawTexturePro(player_texture, src_rec, dst_rec, player_size_half, -1 * RAD2DEG * rot, WHITE); 
	    DrawLineEx(player_pos, GetMousePosition(), 3.0, DEBUGRED1);


