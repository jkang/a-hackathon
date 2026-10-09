# Mac 预装 Checklist

统一路径 `/Users/Shared/a-hackathon`。opencode 从官网直接安装；**项目不联网 git**，从 GitHub 取的东西由**项目方以 zip 包分发**（`agent-reach.zip`、`a-hackathon.zip`），vendor 从本地安装。
装完能跑通 `/run A` 并**用 Chrome 打开**产出即合格。

## 1. 基础环境

### 1.1 网络与设备标识 - vendor在 12号之前提前安装配置好

| 项 | 操作 | 验收 |
|---|---|---|
| 网络 | 连接现场 Wi-Fi，确保能访问公网 | 浏览器能打开网页 |
| 设备标识（唯一名） | 系统设置 → 通用 → 共享 → **电脑名称** 改为统一命名 `G01`、`G02`、`G03`、`G04`…（`组号-A` = 主设备，`-B` = 备用设备） | 名称唯·
| AirDrop | 打开 **Wi-Fi 与蓝牙**；Finder → AirDrop → 「允许被以下人员发现」选 **所有人**（跨 Apple ID 也能互传） | 两台互见并成功传文件 |
| 电源 / 锁屏 | 关闭自动休眠与锁屏（现场演示不中断） | 长时间不锁屏 |
| 设备标识壁纸 | 壁纸上展示设备标识 |直接可以看到电脑标识，方便用 airdrop 传文件 |
| Google Chrome | **打开所有 HTML 产物**；**设为默认浏览器** | `brew install --cask google-chrome` |
| opencode | 主程序 | 官网直接安装：`https://opencode.ai/install` |


### 1.2 工具（用 Homebrew 装）

| 工具 | 用途 | 命令 |
|---|---|---|
| Homebrew | 包管理器 | `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"` |
| Node.js 22 | opencode 运行环境 | `brew install node@22` |
| Python 3.13 | agent-reach 运行环境 | `brew install python@3.13` |
| pipx | 隔离安装 agent-reach | `brew install pipx` |

> `node@22` / `python@3.13` 是 keg-only，写入 PATH 才生效：
> ```bash
> echo 'export PATH="/opt/homebrew/opt/node@22/bin:$PATH"' >> ~/.zprofile
> echo 'export PATH="/opt/homebrew/opt/python@3.13/libexec/bin:$PATH"' >> ~/.zprofile
> source ~/.zprofile
> ```

## 2. opencode、研究引擎与项目包

| 步骤 | 用途 | 操作 |
|---|---|---|
| agent-reach | 实时研究引擎 | `pipx install ~/Downloads/agent-reach.zip`（zip 由项目方提供，即 GitHub 源码包，本地即可安装）后 `agent-reach install --env=auto --system` |
| 项目仓库 | skills / agents / commands | `unzip -q a-hackathon.zip -d /Users/Shared/`（最终为 `/Users/Shared/a-hackathon`） |
| DeepSeek Key | 驱动 AI | `opencode auth login`（选 DeepSeek，粘贴项目方提供的 Key） |
| mcporter | Exa 网页搜索 / 小红书 / 抖音 渠道 | `npm install -g mcporter` |

## 3. 冒烟

### 3.1 Toolkit 链路

在仓库目录启动 opencode，进入 workspace 后**在 opencode 里输入 `/run A`**：

```bash
cd /Users/Shared/a-hackathon
opencode          # 进入 workspace
# 然后在 opencode 提示符输入：/run A
```
产出后用 **Chrome 打开** `artifacts/QuestA-01/proposal.html` 即合格。

### 3.2 Teams 会议接入与屏幕共享

不登录账号、用 Chrome **以访客身份加入** Teams 会议，并测试屏幕共享：

1. Chrome 打开会议链接 → 「**改为在 Web 上加入**」（不要安装桌面客户端）
2. 以访客身份输入姓名 → 进入会议（无需 Microsoft 账号）
3. 点「**共享**」→ 选择屏幕 / 窗口，确认对方能看到（现场路演用）

**注意**：Key 只留本机、不进仓库。
