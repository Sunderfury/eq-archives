
<?xml version="1.0" encoding="Shift-JIS" ?>
<!-- XML�̃o�[�W�����Ǝg�p����̐錾 -->

<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<!-- XSLT�̖��O��� -->


<xsl:comment><!-- XML�����ɃR�����g��}��(���쌠�\�����Ɏg����H) -->
</xsl:comment>

<xsl:element name="�v�f��"><!-- �o�͕����� <�v�f��>�v�f�̓��e</�v�f��> ��}�� -->
</xsl:element>

<xsl:attribute name="������"><!-- ������="�����̒l"�̌`�ŏo�� -->
</xsl:attribute>


<xsl:template match="/" language="�X�N���v�g����">
<!-- "/"�Ƃ�"//"�̓p�^�[���ƌ����B�v�f�����g�p�\ -->
<!-- ��L�̗�̓��[�g�v�f�ɑ΂���(�����Ώ�=�e���v���[�g�̎w��) -->

<xsl:value-of/><!-- ���[�g�ȊO�̗v�f�̒l��S�Ď��o��(��������̎w��) -->

</xsl:template>


<xsl:apply-templates select="�p�^�[��" order-by="�\�[�g�w��"/>
<!-- �e���v���[�g��K�p����v�f�̎w�� -->


<xsl:if test="Item[�i��='��']">�����i�ł���</xsl:if>
<xsl:if test="Item[�i��='��']">�����Ƃ����i�ł���</xsl:if>
<!-- �������� -->



</xsl:stylesheet>