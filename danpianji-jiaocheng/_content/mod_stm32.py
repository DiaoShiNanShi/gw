"""Chapter content definitions."""

from .helpers import chapter

CHAPTERS = {
    "STM32/01-入门.html": chapter(
        'STM32 01：入门',
        'STM32 专题',
        'STM32',
        """<blockquote><p>STM32 家族 F/G/H/L/U，为何工业标准，开发板选择。</p></blockquote><hr>
<h2>1. 家族</h2>
<table><thead><tr><th>系列</th><th>定位</th></tr></thead><tbody><tr><td>F1/F4</td><td>通用主流</td></tr><tr><td>H7</td><td>高性能</td></tr><tr><td>L0/L4</td><td>超低功耗</td></tr><tr><td>U5</td><td>安全+低功耗</td></tr></tbody></table>
<h2>2. 为何学</h2>
<p>求职嵌入式最常见；外设丰富；CubeMX 生态；从 F103 到 H7 路线清晰。</p>
<h2>3. 开发板</h2>
<table><thead><tr><th>板</th><th>特点</th></tr></thead><tbody><tr><td>Blue Pill F103</td><td>12元便宜</td></tr><tr><td>Nucleo</td><td>带ST-Link</td></tr><tr><td>Discovery</td><td>带屏传感器</td></tr></tbody></table>
<h2>4. 首个工程</h2>
<pre><code class="language-c">int main(void){
  HAL_Init(); SystemClock_Config(); MX_GPIO_Init();
  while(1){ HAL_GPIO_TogglePin(GPIOC,GPIO_PIN_13); HAL_Delay(500);}
}</code></pre>
<div class="tip-box">💡 求职嵌入式 STM32 是必修课。</div>
<h2>常见问题</h2>
<h3>F103 过时?</h3><p>入门够用，工业仍大量在用。</p>
<h3>Mac?</h3><p>CubeIDE 有 macOS 版。</p>
<h3>vs ESP32?</h3><p>STM32 控，ESP32 连。</p>
<h2>本章小结</h2><ul>
<li>ST工业标准</li>
<li>F103入门H7高性能</li>
<li>Nucleo带ST-Link</li>
<li>HAL+CubeMX</li>
</ul>
<p><strong>下一步：</strong> <a href="02-CubeMX入门.html">02-CubeMX</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "STM32/02-CubeMX入门.html": chapter(
        'STM32 02：CubeMX 入门',
        'STM32 专题',
        'STM32',
        """<blockquote><p>图形化配时钟/GPIO/UART，生成工程。</p></blockquote><hr>
<h2>1. 流程</h2>
<ol><li>选芯片/NUCLEO</li><li>Pinout 点引脚</li><li>Clock 配 PLL</li><li>Project→Generate</li></ol>
<h2>2. 引脚配置</h2>
<table><thead><tr><th>模式</th><th>用途</th></tr></thead><tbody><tr><td>GPIO_Output</td><td>LED</td></tr><tr><td>GPIO_EXTI</td><td>按键</td></tr><tr><td>USART1</td><td>串口</td></tr><tr><td>I2C1</td><td>传感器</td></tr></tbody></table>
<h2>3. 生成目录</h2>
<pre><code class="language-text">Core/Src/main.c — 用户代码区 USER CODE BEGIN/END
Drivers/ — HAL 库
.ioc — 可重新打开 CubeMX</code></pre>
<h2>4. 规则</h2>
<p>只在 USER CODE 区写逻辑，避免 regenerate 覆盖。</p>
<div class="tip-box">💡 改 .ioc 重新 Generate，别手改 generated 文件。</div>
<h2>常见问题</h2>
<h3>覆盖代码?</h3><p>写 USER CODE 区内。</p>
<h3>时钟红叉?</h3><p>PLL 倍频超规格。</p>
<h3>HAL vs LL?</h3><p>HAL 易用 LL 高效。</p>
<h2>本章小结</h2><ul>
<li>CubeMX 配引脚时钟</li>
<li>Generate 生成 HAL</li>
<li>USER CODE 区写逻辑</li>
<li>.ioc 可版本管理</li>
</ul>
<p><strong>下一步：</strong> <a href="03-时钟树配置.html">03-时钟</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "STM32/03-时钟树配置.html": chapter(
        'STM32 03：时钟树配置',
        'STM32 专题',
        'STM32',
        """<blockquote><p>HSE/HSI、PLL 倍频、APB 分频、SystemCoreClock。</p></blockquote><hr>
<h2>1. 时钟源</h2>
<table><thead><tr><th>源</th><th>频率</th><th>用途</th></tr></thead><tbody><tr><td>HSE</td><td>8MHz 晶振</td><td>精确</td></tr><tr><td>HSI</td><td>8MHz RC</td><td>备用</td></tr><tr><td>PLL</td><td>倍频</td><td>系统主频</td></tr></tbody></table>
<h2>2. 72MHz 示例</h2>
<pre><code class="language-text">HSE 8MHz → PLL ×9 → SYSCLK 72MHz
AHB /1 → 72MHz
APB1 /2 → 36MHz (定时器×2=72)
APB2 /1 → 72MHz</code></pre>
<h2>3. 影响</h2>
<p>SystemCoreClock 错 → HAL_Delay/波特率/SysTick 全错。UART 波特率=PCLK/(16×USARTDIV)。</p>
<h2>4. 验证</h2>
<pre><code class="language-c">printf("SYSCLK=%lu\\n", HAL_RCC_GetSysClockFreq());</code></pre>
<div class="tip-box">💡 Delay 不对先查时钟树。</div>
<h2>常见问题</h2>
<h3>HSI vs HSE?</h3><p>HSE 精度高，HSI 免晶振。</p>
<h3>APB 定时器?</h3><p>分频≠1时定时器时钟×2。</p>
<h3>低功耗?</h3><p>降频+关外设时钟。</p>
<h2>本章小结</h2><ul>
<li>时钟决定一切延时</li>
<li>PLL 倍频到目标</li>
<li>APB 分频影响定时器</li>
<li>printf 验证频率</li>
</ul>
<p><strong>下一步：</strong> <a href="04-GPIO与HAL.html">04-GPIO</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "STM32/04-GPIO与HAL.html": chapter(
        'STM32 04：GPIO 与 HAL',
        'STM32 专题',
        'STM32',
        """<blockquote><p>推挽/开漏/上拉/速度，HAL_GPIO 读写。</p></blockquote><hr>
<h2>1. HAL API</h2>
<pre><code class="language-c">HAL_GPIO_WritePin(GPIOC, GPIO_PIN_13, GPIO_PIN_SET);
GPIO_PinState s = HAL_GPIO_ReadPin(GPIOC, GPIO_PIN_13);
HAL_GPIO_TogglePin(GPIOC, GPIO_PIN_13);</code></pre>
<h2>2. 初始化结构</h2>
<pre><code class="language-c">GPIO_InitTypeDef g={0};
g.Pin=GPIO_PIN_13; g.Mode=GPIO_MODE_OUTPUT_PP;
g.Pull=GPIO_NOPULL; g.Speed=GPIO_SPEED_FREQ_LOW;
HAL_GPIO_Init(GPIOC, &g);</code></pre>
<h2>3. 模式</h2>
<table><thead><tr><th>模式</th><th>场景</th></tr></thead><tbody><tr><td>OUTPUT_PP</td><td>LED</td></tr><tr><td>INPUT_PULLUP</td><td>按键</td></tr><tr><td>OUTPUT_OD</td><td>I2C</td></tr><tr><td>AF_PP</td><td>UART/SPI</td></tr></tbody></table>
<h2>4. BSRR 寄存器</h2>
<p>HAL 底层写 BSRR 原子置位/复位，避免读-改-写竞态。</p>
<div class="tip-box">💡 AF 模式由 CubeMX 配，别手动改除非懂 remap。</div>
<h2>常见问题</h2>
<h3>读 WritePin?</h3><p>用 ReadPin。</p>
<h3>速度 LOW/HIGH?</h3><p>高速边沿陡，可能 EMI。</p>
<h3>JTAG 占脚?</h3><p>Disable SWD 释放。</p>
<h2>本章小结</h2><ul>
<li>HAL_GPIO 三件套</li>
<li>PP/OD/AF 模式</li>
<li>BSRR 原子操作</li>
<li>CubeMX 生成 Init</li>
</ul>
<p><strong>下一步：</strong> <a href="05-UART驱动.html">05-UART</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "STM32/05-UART驱动.html": chapter(
        'STM32 05：UART 驱动',
        'STM32 专题',
        'STM32',
        """<blockquote><p>HAL_UART_Transmit/Receive，printf 重定向，DMA。</p></blockquote><hr>
<table><thead><tr><th>要点</th><th>说明</th></tr></thead><tbody><tr><td>实验</td><td>DevKit 验证</td></tr><tr><td>调试</td><td>串口 printf</td></tr></tbody></table>
<h2>1. 阻塞发送</h2>
<pre><code class="language-c">uint8_t msg[]="Hello\\r\\n";
HAL_UART_Transmit(&huart1, msg, sizeof(msg)-1, 100);</code></pre>
<h2>2. printf 重定向</h2>
<pre><code class="language-c">int _write(int fd, char *ptr, int len){
  HAL_UART_Transmit(&huart1,(uint8_t*)ptr,len,HAL_MAX_DELAY);
  return len;
}</code></pre>
<h2>3. 中断接收</h2>
<pre><code class="language-c">HAL_UART_Receive_IT(&huart1, &rx_byte, 1);
void HAL_UART_RxCpltCallback(UART_HandleTypeDef *huart){
  // 处理 rx_byte; 再启动 Receive_IT
}</code></pre>
<h2>4. 波特率</h2>
<p>115200 8N1；PCLK 变化需重算 USARTDIV。</p>
<div class="tip-box">💡 RX 中断里别阻塞，快速入队。</div>
<h2>常见问题</h2>
<h3>printf 无输出?</h3><p>检查 _write 链接。</p>
<h3>乱码?</h3><p>时钟/波特率。</p>
<h3>DMA?</h3><p>大缓冲高效收发。</p>
<h2>本章小结</h2><ul>
<li>HAL_UART 阻塞/中断/DMA</li>
<li>_write 重定向 printf</li>
<li>RxCpltCallback 链式接收</li>
<li>115200 8N1</li>
</ul>
<p><strong>下一步：</strong> <a href="06-SPI驱动.html">06-SPI</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "STM32/06-SPI驱动.html": chapter(
        'STM32 06：SPI 驱动',
        'STM32 专题',
        'STM32',
        """<blockquote><p>HAL_SPI_TransmitReceive，W25Q Flash 读 ID。</p></blockquote><hr>
<table><thead><tr><th>要点</th><th>说明</th></tr></thead><tbody><tr><td>实验</td><td>DevKit 验证</td></tr><tr><td>调试</td><td>串口 printf</td></tr></tbody></table>
<h2>1. 全双工</h2>
<pre><code class="language-c">uint8_t tx[2]={0x9F,0xFF}, rx[2]={0};
HAL_SPI_TransmitReceive(&hspi1, tx, rx, 2, 100);
// rx[1] 可能是 Flash 制造商 ID</code></pre>
<h2>2. CS 控制</h2>
<pre><code class="language-c">HAL_GPIO_WritePin(GPIOA, CS_Pin, GPIO_PIN_RESET);
HAL_SPI_Transmit(&hspi1, cmd, len, 100);
HAL_GPIO_WritePin(GPIOA, CS_Pin, GPIO_PIN_SET);</code></pre>
<h2>3. 模式</h2>
<p>CubeMX 选 Mode0-3 对应 CPOL/CPHA，与 Flash 手册一致。</p>
<h2>4. 速率</h2>
<p>分频器调 SCK；PCB 长线降速加匹配。</p>
<div class="tip-box">💡 SPI 模式不对读到 0xFF/0x00。</div>
<h2>常见问题</h2>
<h3>只发不收?</h3><p>Transmit 或 TX 填 0xFF。</p>
<h3>DMA SPI?</h3><p>大数据块用。</p>
<h3>3线?</h3><p>半双工 MISO/MOSI 共用。</p>
<h2>本章小结</h2><ul>
<li>TransmitReceive 全双工</li>
<li>软件控 CS</li>
<li>模式查 slave 手册</li>
<li>降速排查波形</li>
</ul>
<p><strong>下一步：</strong> <a href="07-I2C驱动.html">07-I2C</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "STM32/07-I2C驱动.html": chapter(
        'STM32 07：I2C 驱动',
        'STM32 专题',
        'STM32',
        """<blockquote><p>HAL_I2C_Mem_Read/Write，OLED/EEPROM。</p></blockquote><hr>
<h2>1. 写寄存器</h2>
<pre><code class="language-c">HAL_I2C_Mem_Write(&hi2c1, 0x3C<<1, 0x00, I2C_MEMADD_SIZE_8BIT, &cmd, 1, 100);</code></pre>
<h2>2. 读传感器</h2>
<pre><code class="language-c">uint8_t reg=0xF7; uint8_t buf[6];
HAL_I2C_Mem_Write(&hi2c1, BME_ADDR, reg, 1, &reg, 1, 100);
HAL_I2C_Mem_Read(&hi2c1, BME_ADDR, reg, 1, buf, 6, 100);</code></pre>
<h2>3. 扫描</h2>
<p>HAL_I2C_IsDeviceReady(&hi2c1, addr<<1, 3, 10) 试地址。</p>
<h2>4. 错误</h2>
<table><thead><tr><th>现象</th><th>原因</th></tr></thead><tbody><tr><td>HAL_BUSY</td><td>总线死锁，重新 Init</td></tr><tr><td>NACK</td><td>地址/上拉/供电</td></tr></tbody></table>
<div class="tip-box">💡 I2C 死锁可 clock 9 脉冲或 reinit。</div>
<h2>常见问题</h2>
<h3>7位地址?</h3><p>HAL 左移1位+R/W。</p>
<h3>400kHz?</h3><p>Fast Mode 加上拉。</p>
<h3>SMBus?</h3><p>I2C 子集带超时。</p>
<h2>本章小结</h2><ul>
<li>Mem_Read/Write 带寄存器地址</li>
<li>IsDeviceReady 扫描</li>
<li>NACK查地址上拉</li>
<li>400k 需强上拉</li>
</ul>
<p><strong>下一步：</strong> <a href="08-ADC与DMA.html">08-ADC</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "STM32/08-ADC与DMA.html": chapter(
        'STM32 08：ADC 与 DMA',
        'STM32 专题',
        'STM32',
        """<blockquote><p>多通道扫描+DMA 环缓冲，音频/波形采集。</p></blockquote><hr>
<h2>1. 配置</h2>
<p>ADC1 多通道 scan + DMA circular mode → 缓冲区自动更新。</p>
<h2>2. 启动</h2>
<pre><code class="language-c">HAL_ADC_Start_DMA(&hadc1, (uint32_t*)adc_buf, ADC_BUF_LEN);
// 半满/全满回调处理数据</code></pre>
<h2>3. 电压换算</h2>
<pre><code class="language-c">float v = adc_buf[i] * 3.3f / 4095.0f;</code></pre>
<h2>4. vs 轮询</h2>
<table><thead><tr><th>方式</th><th>CPU</th><th>场景</th></tr></thead><tbody><tr><td>Poll</td><td>阻塞</td><td>单次读</td></tr><tr><td>DMA</td><td>几乎零占用</td><td>连续采样</td></tr></tbody></table>
<div class="tip-box">💡 DMA 缓冲用 volatile 或 cache invalidate (H7)。</div>
<h2>常见问题</h2>
<h3>采样率?</h3><p>ADC clock+采样周期。</p>
<h3>参考电压?</h3><p>VDDA 或 VREFINT 校准。</p>
<h3>双ADC?</h3><p>同步采样。</p>
<h2>本章小结</h2><ul>
<li>Scan+DMA 连续采集</li>
<li>Circular 环缓冲</li>
<li>半满回调处理</li>
<li>省 CPU 做滤波</li>
</ul>
<p><strong>下一步：</strong> <a href="09-定时器与PWM.html">09-PWM</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "STM32/09-定时器与PWM.html": chapter(
        'STM32 09：定时器与 PWM',
        'STM32 专题',
        'STM32',
        """<blockquote><p>TIM PWM 模式，频率占空比，舵机/电机。</p></blockquote><hr>
<table><thead><tr><th>要点</th><th>说明</th></tr></thead><tbody><tr><td>实验</td><td>DevKit 验证</td></tr><tr><td>调试</td><td>串口 printf</td></tr></tbody></table>
<h2>1. PWM 公式</h2>
<pre><code class="language-text">freq = TIM_CLK / ((PSC+1)*(ARR+1))
duty = (CCR+1)/(ARR+1)</code></pre>
<h2>2. 启动</h2>
<pre><code class="language-c">HAL_TIM_PWM_Start(&htim2, TIM_CHANNEL_1);
__HAL_TIM_SET_COMPARE(&htim2, TIM_CHANNEL_1, 750); // 75% duty</code></pre>
<h2>3. 舵机 50Hz</h2>
<p>ARR 定 20ms 周期，CCR 1-2ms 脉宽。</p>
<h2>4. 输入捕获</h2>
<p>测外部脉冲宽度，超声波/编码器。</p>
<div class="tip-box">💡 高级定时器 TIM1/8 可驱动电机互补 PWM+死区。</div>
<h2>常见问题</h2>
<h3>PSC ARR?</h3><p>预分频与自动重装。</p>
<h3>互补输出?</h3><p>H桥电机。</p>
<h3>编码器模式?</h3><p>TIM 硬件解码。</p>
<h2>本章小结</h2><ul>
<li>PSC/ARR 定频率</li>
<li>CCR 定占空比</li>
<li>50Hz 舵机标准</li>
<li>输入捕获测脉宽</li>
</ul>
<p><strong>下一步：</strong> <a href="10-看门狗.html">10-看门狗</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "STM32/10-看门狗.html": chapter(
        'STM32 10：看门狗',
        'STM32 专题',
        'STM32',
        """<blockquote><p>IWDG/WWDG，喂狗策略，防死机。</p></blockquote><hr>
<table><thead><tr><th>要点</th><th>说明</th></tr></thead><tbody><tr><td>实验</td><td>DevKit 验证</td></tr><tr><td>调试</td><td>串口 printf</td></tr></tbody></table>
<h2>1. 独立 IWDG</h2>
<p>LSI 驱动，一旦启动无法停止，超时复位。适合防程序跑飞。</p>
<h2>2. 窗口 WWDG</h2>
<p>必须在窗口内喂狗，太早太晚都复位。</p>
<h2>3. 喂狗</h2>
<pre><code class="language-c">HAL_IWDG_Init(&hiwdg);
while(1){ /* 主循环 */ HAL_IWDG_Refresh(&hiwdg); }</code></pre>
<h2>4. 策略</h2>
<p>只在「健康路径」喂狗；卡死在中断/死循环则复位恢复。</p>
<div class="tip-box">💡 调试时可暂时不启 IWDG，量产必须开。</div>
<h2>常见问题</h2>
<h3>喂狗间隔?</h3><p>看超时配置。</p>
<h3>RTOS?</h3><p>Idle hook 或专用任务喂。</p>
<h3>复位原因?</h3><p>RCC flag 读 IWDG reset。</p>
<h2>本章小结</h2><ul>
<li>IWDG 独立看门狗</li>
<li>主循环健康才喂</li>
<li>RTOS 专用任务喂</li>
<li>读 flag 知复位原因</li>
</ul>
<p><strong>下一步：</strong> <a href="../ESP32/01-入门与STM32对比.html">ESP32 01</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
}
