import streamlit as st
import numpy as np

# Title
st.title("Wearable Ultrasound System GUI")

# Sidebar for Navigation
st.sidebar.title("Navigation")

menu = st.sidebar.radio("Go to:", ["MUX/PCF (TMUX7349/PCF8574)", 
                                   "Pulser (MAX14813)", 
                                   "Ultrasound Receiver (AFE5401)", 
                                   "FIFO (72V36110)", 
                                   "Wi-Fi Module", 
                                   "Si5351"])

wifi_gpio_pins = [i for i in range(1,11)]


# MUX (TMUX7349) Section
if menu == "MUX/PCF (TMUX7349/PCF8574)":
    st.header("MUX/PCF Configuration")
    pcf_i2c_sda_pin = st.selectbox("I2C_SDA_PIN in wifi", wifi_gpio_pins)
    pcf_i2c_scl_pin = st.selectbox("I2C_SCL_PIN in wifi", wifi_gpio_pins)
    pcf_pattern_switch_freq = st.number_input("Set Pattern switch Frequency (KHz)", min_value=0.5, max_value=5.0, step=0.5)
    st.write(f"WIFI pins: i2c_sda {pcf_i2c_sda_pin} i2c_scl {pcf_i2c_scl_pin} pcf_pattern_switch_freq {pcf_pattern_switch_freq} KHz")

# Pulser (MAX14813) Section
elif menu == "Pulser (MAX14813)":
    st.header("Pulser Configuration")
    tx_spi_mosi             = st.selectbox("SPI_MOSI", wifi_gpio_pins)
    tx_spi_miso             = st.selectbox("SPI_MISO", wifi_gpio_pins)
    tx_spi_sclk             = st.selectbox("SPI_SCLK", wifi_gpio_pins)
    tx_spi_cs               = st.selectbox("SPI_CS", wifi_gpio_pins)
    tx_spi_clk              = st.number_input("SPI clk(MHz)", min_value=0.5, max_value=2.5, step=0.5)
    tx_pattern_time_period  = st.number_input("TX pattern time period (us)", min_value=500.0, max_value=1500.0, step=100.0)
    tx_clk_in_freq          = st.number_input("TX clk out frequency (kHZ)", min_value=50.0, max_value=200.0, step=10.0)
    pwt_length              = (tx_pattern_time_period/1000.0) * tx_clk_in_freq
    st.write(f"SPI_MOSI: {tx_spi_mosi} SPI_MISO: {tx_spi_miso}, pwt_length: {pwt_length}")

# Ultrasound Receiver (AFE5401) Section
elif menu == "Ultrasound Receiver (AFE5401)":
    st.header("Ultrasound Receiver Configuration")
    # Choose SPI pins
    rx_spi_mosi             = st.selectbox("SPI_MOSI", wifi_gpio_pins)
    rx_spi_miso             = st.selectbox("SPI_MISO", wifi_gpio_pins)
    rx_spi_sclk             = st.selectbox("SPI_SCLK", wifi_gpio_pins)
    rx_spi_cs               = st.selectbox("SPI_CS", wifi_gpio_pins)
    dsync_en_register       = st.text_input("DSYNC_EN_REG_VAL")
    sample_count_register   = st.text_input("SAMPLE_COUNT_REG_VAL")
    out_mode_en_register    = st.text_input("OUT_MODE_EN_REG_VAL")
    rx_clk_in_frequency     = st.number_input("Set Clock Frequency (MHz)", min_value=10.0, max_value=100.0, step=5.0)
    #gain = st.slider("Set Gain", 0, 100, 50)
    #high_pass = st.selectbox("High-Pass Filter Cutoff", ["10 kHz", "20 kHz", "50 kHz"])
    #low_pass = st.selectbox("Low-Pass Filter Cutoff", ["100 kHz", "200 kHz", "500 kHz"])
    #st.write(f"Gain: {gain}, High-Pass: {high_pass}, Low-Pass: {low_pass}")
    st.write(f"SPI_MOSI: {rx_spi_mosi} SPI_MISO: {rx_spi_miso} dsync {dsync_en_register} sample count {sample_count_register} out mode {out_mode_en_register} clk in freq {rx_clk_in_frequency}")

# FIFO (72V36110) Section
elif menu == "FIFO (72V36110)":
    st.header("FIFO Configuration")
    fifo_rd_clk = st.number_input("Set FIFO read clk (MHz)", min_value=25.0, max_value=250.0, step=25.0)
    fifo_wr_clk = st.number_input("Set FIFO write clk (MHz)", min_value=25.0, max_value=250.0, step=25.0)
    #fifo_depth = st.number_input("Set FIFO Depth", min_value=0, max_value=2048, step=1, value=1024)
    st.write(f"FIFO read clk: {fifo_rd_clk} MHz FIFO write clk {fifo_wr_clk} MHz")

# Wi-Fi Module Section
elif menu == "Wi-Fi Module":
    st.write("TBD for wifi")

# Si5351 Section
elif menu == "Si5351":
    st.header("Si5351 Configuration")
    si_clk_in_freq = st.number_input("Clock in frequency (MHz)", min_value=1.0, max_value=20.0, step=1.0)
    si_num_out_clks = st.number_input("Num output clocks", min_value=1, max_value=10)
    si_clk_out_freq_val = [i for i in range(1, si_num_out_clks+1)]
    si_clk_out_freq_unit= [i for i in range(1, si_num_out_clks+1)]
    for i in range(0, si_num_out_clks):
        si_clk_out_freq_unit[i] = st.radio(f"Clock out {i+1} freq unit", ["kHZ", "MHz"])
        si_clk_out_freq_val[i] = st.slider(f"Clock out {i+1} freq value", 1, 100, 1)
    msg = ""
    for i in range(0, si_num_out_clks):
        msg = f"{msg} ||  Clk {i+1} output frequency: {si_clk_out_freq_val[i]} {si_clk_out_freq_unit[i]}"
    st.write(msg)
# Footer
st.sidebar.write("Developed with Streamlit")