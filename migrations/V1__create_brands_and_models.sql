-- V1__create_brands_and_models.sql

-- Crear tabla "brands"
CREATE TABLE brands (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL
);

-- Crear tabla "models"
CREATE TABLE models (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    average_price FLOAT,
    brand_id INT,
    CONSTRAINT fk_brand FOREIGN KEY (brand_id) REFERENCES brands(id) ON DELETE SET NULL
);

-- Crear índices en las tablas
CREATE INDEX idx_brand_name ON brands (name);
CREATE INDEX idx_model_name ON models (name);
CREATE INDEX idx_model_brand_id ON models (brand_id);
