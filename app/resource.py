from import_export import resources
from import_export.fields import Field
from .models import Pembayaran

class PembayaranResource(resources.ModelResource):
    tgl_bayar = Field(attribute='tgl_bayar', column_name='Tanggal')
    waktu_dibayar = Field(attribute='waktu_dibayar', column_name='Pukul')
    id_spp = Field(attribute='id_spp', column_name='SPP')
    jumlah_bayar = Field(attribute='jumlah_bayar', column_name='Jumlah Bayar')
    metode_pembayaran = Field(attribute='metode_pembayaran', column_name='Metode Pembayaran')

    class Meta:
        model = Pembayaran
        fields = ['tgl_bayar', 'waktu_dibayar', 'id_spp', 'jumlah_bayar', 'metode_pembayaran']