CREATE TABLE User (
    id INT AUTO_INCREMENT PRIMARY KEY,             -- 用户ID，自增主键
    email VARCHAR(50) NOT NULL UNIQUE,               -- 邮箱
    password VARCHAR(255) NOT NULL,                 -- 密码（存储哈希值）
    nickname VARCHAR(50) NOT NULL,                  -- 昵称
    gender ENUM('male', 'female', 'other') DEFAULT 'other', -- 性别
    age INT,                                        -- 年龄
    contact VARCHAR(100),                           -- 联系方式
    reputation INT DEFAULT 0,                       -- 信誉积分
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP    -- 账户创建时间
);

CREATE TABLE Commodity (
    id INT AUTO_INCREMENT PRIMARY KEY,             -- 商品ID
    user_id INT NOT NULL,                           -- 发布商品的用户ID
    name VARCHAR(100) NOT NULL,                     -- 商品名称
    description TEXT,                               -- 商品描述
    price DECIMAL(10, 2) NOT NULL,                  -- 商品价格
    category VARCHAR(50),                           -- 商品分类
    status ENUM('available', 'sold', 'removed') DEFAULT 'available', -- 商品状态
    image VARCHAR(255),                             -- 商品图片链接
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- 商品创建时间
    updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- 商品更新时间
    FOREIGN KEY (user_id) REFERENCES User(id)       -- 外键关联用户表
);

CREATE TABLE Record (
    id INT AUTO_INCREMENT PRIMARY KEY,             -- 交易记录ID
    buyer_id INT NOT NULL,                          -- 买家ID
    seller_id INT NOT NULL,                         -- 卖家ID
    commodity_id INT NOT NULL,                      -- 商品ID
    quantity INT NOT NULL,                          -- 购买数量
    total DECIMAL(10, 2) NOT NULL,                  -- 交易总价
    status ENUM('pending', 'accepted', 'completed', 'canceled') DEFAULT 'pending', -- 交易状态
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- 交易创建时间
    updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- 交易更新时间
    FOREIGN KEY (buyer_id) REFERENCES User(id),     -- 外键关联买家
    FOREIGN KEY (seller_id) REFERENCES User(id),    -- 外键关联卖家
    FOREIGN KEY (commodity_id) REFERENCES Commodity(id) -- 外键关联商品
);

