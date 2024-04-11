/*
    this is the code to center fit an image in kitty terminal.
        -> Kitty_terminal_center_fit_image.png
    the code works but it's not properly integrated. 
    this code goes in shaders.c and overwrites the CENTER_SCALED option. 
*/


case CENTER_SCALED: {

    if (iheight > iwidth) {
        GLfloat niw = iwidth / iheight * vheight / vwidth;
        GLfloat trim = (1.0f - niw);
        left = -1.0f + trim;   // wfrac;
        right = 1.0f - trim;   // wfrac;
    }

    if (iheight <= iwidth) {
        GLfloat nih = iheight / iwidth * vwidth / vheight;
        GLfloat trim = (1.0f - nih);
        top = 1.0f - trim;
        bottom = -1.0f + trim;
    }
  } break;
