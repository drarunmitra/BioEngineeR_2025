img_path <- here("figures", "BioEngineeR2026_hex_hires.png")

sticker(
    subplot = img_path,
    package = "",
    p_size = 18,
    p_y = 1.45,
    p_color = "#FFFFFF",
    p_family = "firasans",
    s_x = 1.01,
    s_y = 1, # Adjusted position for background image
    s_width = 1.05, # Default width, adjustable
    s_height = 1.05,
    h_fill = "#1b574bed", # Dark background to match previous theme
    h_color = "#1b574bed",
    h_size = 1.5,
    url = "https://drarunmitra.github.io/BioEngineeR_2026/",
    u_color = "#CCCCCC",
    u_size = 3.2,
    u_x = 1.1,
    u_y = 0.07,
    filename = here("figures", "BioEngineeR2026_final.png"),
    dpi = 300,
    white_around_sticker = TRUE
)


sticker(
    subplot = img_path,
    package = "",
    p_size = 18,
    p_y = 1.45,
    p_color = "#FFFFFF",
    p_family = "firasans",
    s_x = 1.01,
    s_y = 1, # Adjusted position for background image
    s_width = 1.1, # Default width, adjustable
    s_height = 1.1,
    h_fill = "#00000000", # Dark background to match previous theme
    h_color = "#00000000",
    h_size = 1.5,
    url = "https://drarunmitra.github.io/BioEngineeR_2026/",
    u_color = "black",
    u_size = 3.2,
    u_x = 1.05,
    u_y = 0.055,
    filename = here("figures", "BioEngineeR2026_final.png"),
    dpi = 300,
    white_around_sticker = FALSE
)
