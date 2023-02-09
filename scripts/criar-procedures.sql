-- Criar procedure responsável por atualizar o custo do procedimento de acordo com o 
-- código do procedimento.
DELIMITER $$
CREATE PROCEDURE atualizaCustoProcedimento (IN cod INT, IN custoNovo DECIMAL(10, 0))
BEGIN
  DECLARE custoAntigo DECIMAL(10, 0);
  SELECT custo INTO custoAntigo FROM PROCEDIMENTO WHERE codigo = cod;
  
  IF custoNovo <= 0 THEN
    SELECT 'Custo inválido, digite um valor maior ou igual a 0';
  ELSE
    UPDATE PROCEDIMENTO SET custo = custoNovo WHERE codigo = cod;
    SELECT 'O custo do procedimento foi atualizado de '+custoAntigo+' para '+custoNovo;
  END IF;
END $$
DELIMITER ;